import sys
print(f"Python {sys.version.split()[0]}\n")

# Список для проверки
libs_to_test = [
    ("tensorflow","2.13"),
    ("numpy", "1.24.3"),
    ("scipy", "1.10.1"),
    ("sklearn", "1.2.2"),
    ("pandas", None),
    ("matplotlib", None),
    ("seaborn", None)    
]

for lib_name, expected_version in libs_to_test:
    try:
        if lib_name == "tensorflow":
            import tensorflow as lib
        elif lib_name == "sklearn":
            import sklearn as lib
        elif lib_name == "imblearn":
            import imblearn as lib
        else:
            lib = __import__(lib_name)
        
        version = getattr(lib, '__version__', 'unknown')
        
        if expected_version and version == expected_version:
            print(f"✅ {lib_name}=={version}")
        elif expected_version:
            print(f"⚠  {lib_name}: {version} (ожидалось {expected_version})")
        else:
            print(f"✅ {lib_name}: {version}")
            
    except ImportError as e:
        print(f"❌ {lib_name}: {e}")
    except Exception as e:
        print(f"❌ {lib_name} ошибка: {e}")

