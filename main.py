def main():
    while True:
        print("\n=== Dev Toolbox ===")
        print("1. Sound Converter (Audio to WAV for now)")
        print("2. Video Converter")
        print("3. Base Converter")
        print("4. File Hasher")
        print("5. File Info File")
        print("6. File Info Directory")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            from dev_tools.sound_converter import run_audio_converter
            run_audio_converter()
            break
        elif choice == "2":
            print("Video Converter: (Coming soon)")
        elif choice == "3":
            from base_converter import run_base_converter
            print(run_base_converter())
            break
        elif choice == "4":
            print("File Hasher: (Coming soon!)")
        elif choice == "5":
            from file_info import get_file_info_single
            print(get_file_info_single(input("Enter the path to the input file"), input("Do you want to use IEC standard (leave blank to use SI)")))
            break
        elif choice == "6":
            from file_info import get_file_info_multi, save_info_to_json
            result = get_file_info_multi(input("Enter the path to the input directory"), input("Do you want to use IEC standard (leave blank to use SI)"))
            save_info_to_json(result, input("Enter where you want the .json to be output"))
            break
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again!")

if __name__ == "__main__":
    main()
