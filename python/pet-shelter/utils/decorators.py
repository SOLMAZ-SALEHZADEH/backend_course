def animal_action(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 35)
        print("🐾  PET SHELTER MANAGEMENT  🐾")
        print(f"🐶  Starting: {func.__name__.replace('_', ' ').title()}")
        print("=" * 35)

        result = func(*args, **kwargs)

        print("=" * 35 + "\n")

        return result

    return wrapper