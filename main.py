from dog_api import list_all_breeds, random_image_any, random_image_by_breed

def print_menu():
    print("Dog Pic Browser")
    print("1) Random dog image")
    print("2) List breeds")
    print("3) Random image by breed")
    print("4) Exit")

def main():
    breeds_cache = None

    while True:
        print_menu()
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                print("\nImage URL:", random_image_any(), "\n")

            elif choice == "2":
                breeds_cache = list_all_breeds()
                print("\nBreeds:")
                print(", ".join(sorted(breeds_cache.keys())))
                print()

            elif choice == "3":
                if breeds_cache is None:
                    # not required, but helps validation
                    breeds_cache = list_all_breeds()

                breed = input("Enter breed (example: hound): ").strip().lower()

                if breed not in breeds_cache:
                    print("\n❌ Unknown breed. Tip: choose option (2) to list breeds.\n")
                    continue

                print("\nImage URL:", random_image_by_breed(breed), "\n")

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("\n❌ Invalid option.\n")

        except Exception as e:
            # keep it demo-friendly
            print(f"\n❌ Error: {e}\n")

if __name__ == "__main__":
    main()
