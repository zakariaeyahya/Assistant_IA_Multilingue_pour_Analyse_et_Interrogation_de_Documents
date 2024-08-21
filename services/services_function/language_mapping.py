# File: services/services_function/language_mapping.py

def get_language_code(language):
    language_map = {
        "français": "fra",
        "anglais": "eng",
        "darija": "ary",
        "arabe": "arb"
    }
    return language_map.get(language.lower(), language)

def get_language_name(code):
    code_map = {
        "fra": "français",
        "eng": "anglais",
        "ary": "darija",
        "arb": "arabe"
    }
    return code_map.get(code.lower(), code)