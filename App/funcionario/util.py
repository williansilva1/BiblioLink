from App import bcrypt

def hash_pass(password):
    """Hash a password for storing."""
    pwdhash = bcrypt.generate_password_hash(password).decode('utf-8')
    return pwdhash

def verify_pass(senha_bd, senha_digitada):
    return bcrypt.check_password_hash(senha_bd, senha_digitada)