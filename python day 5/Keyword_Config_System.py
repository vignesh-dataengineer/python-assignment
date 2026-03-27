def system_configuration(**settings):
    print("\nSystem Configuration:")
    for key, value in settings.items():
        print(f"{key}: {value}")

system_configuration(mode="debug", version="1.0")