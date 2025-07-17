"""
Validadores para formulários da aplicação
"""
import re
from typing import Dict, List, Optional

class FormValidator:
    """Classe para validação de formulários"""
    
    @staticmethod
    def validate_email(email: str) -> tuple[bool, Optional[str]]:
        """
        Valida formato de email
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not email:
            return False, "Email é obrigatório"
        
        # Regex para validação básica de email
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_pattern, email):
            return False, "Formato de email inválido"
        
        if len(email) > 254:  # RFC 5321 limit
            return False, "Email muito longo"
        
        return True, None
    
    @staticmethod
    def validate_name(name: str) -> tuple[bool, Optional[str]]:
        """
        Valida nome
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not name:
            return False, "Nome é obrigatório"
        
        name = name.strip()
        
        if len(name) < 2:
            return False, "Nome deve ter pelo menos 2 caracteres"
        
        if len(name) > 100:
            return False, "Nome muito longo (máximo 100 caracteres)"
        
        # Verifica se contém apenas letras, espaços e caracteres acentuados
        if not re.match(r'^[a-zA-ZÀ-ÿ\s\-\'\.]+$', name):
            return False, "Nome contém caracteres inválidos"
        
        return True, None
    
    @staticmethod
    def validate_message(message: str) -> tuple[bool, Optional[str]]:
        """
        Valida mensagem
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not message:
            return False, "Mensagem é obrigatória"
        
        message = message.strip()
        
        if len(message) < 10:
            return False, "Mensagem deve ter pelo menos 10 caracteres"
        
        if len(message) > 2000:
            return False, "Mensagem muito longa (máximo 2000 caracteres)"
        
        # Verifica se não é apenas espaços ou caracteres repetitivos
        if len(set(message.replace(' ', '').replace('\n', ''))) < 3:
            return False, "Mensagem deve conter conteúdo significativo"
        
        return True, None
    
    @staticmethod
    def detect_spam_patterns(text: str) -> tuple[bool, Optional[str]]:
        """
        Detecta padrões de spam na mensagem
        
        Returns:
            tuple: (is_spam, reason)
        """
        text_lower = text.lower()
        
        # Lista de padrões de spam
        spam_patterns = [
            r'http[s]?://',  # URLs
            r'www\.',        # URLs sem protocolo
            r'\b\d{10,}\b',  # Números de telefone muito longos
            r'(click here|clique aqui)',
            r'(buy now|compre agora)',
            r'(free|grátis|gratuito).{0,20}(money|dinheiro)',
            r'(urgent|urgente)',
            r'(congratulations|parabéns).{0,20}(winner|ganhador)',
        ]
        
        for pattern in spam_patterns:
            if re.search(pattern, text_lower):
                return True, f"Conteúdo suspeito detectado"
        
        # Verifica repetição excessiva de caracteres
        if re.search(r'(.)\1{10,}', text):
            return True, "Muitos caracteres repetidos"
        
        # Verifica se tem muitas palavras em maiúscula
        words = text.split()
        if len(words) > 5:
            upper_words = sum(1 for word in words if word.isupper() and len(word) > 2)
            if upper_words / len(words) > 0.5:
                return True, "Muitas palavras em maiúscula"
        
        return False, None
    
    @classmethod
    def validate_contact_form(cls, data: Dict[str, str]) -> Dict[str, List[str]]:
        """
        Valida formulário de contato completo
        
        Args:
            data: Dicionário com os dados do formulário
            
        Returns:
            Dict com erros encontrados por campo
        """
        errors = {}
        
        # Valida nome
        name = data.get('name', '').strip()
        is_valid, error = cls.validate_name(name)
        if not is_valid:
            errors['name'] = [error]
        
        # Valida email
        email = data.get('email', '').strip()
        is_valid, error = cls.validate_email(email)
        if not is_valid:
            errors['email'] = [error]
        
        # Valida mensagem
        message = data.get('message', '').strip()
        is_valid, error = cls.validate_message(message)
        if not is_valid:
            errors['message'] = [error]
        else:
            # Verifica spam apenas se a mensagem é válida
            is_spam, spam_reason = cls.detect_spam_patterns(message)
            if is_spam:
                if 'message' not in errors:
                    errors['message'] = []
                errors['message'].append(spam_reason)
        
        return errors
    
    @staticmethod
    def sanitize_input(text: str) -> str:
        """
        Sanitiza entrada do usuário removendo caracteres potencialmente perigosos
        
        Args:
            text: Texto a ser sanitizado
            
        Returns:
            Texto sanitizado
        """
        if not text:
            return ""
        
        # Remove caracteres de controle
        text = ''.join(char for char in text if ord(char) >= 32 or char in '\n\r\t')
        
        # Remove múltiplos espaços
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
