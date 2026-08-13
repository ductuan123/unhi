input_file = input("Nhap duong dan file: ").strip().strip('"')
output_file = "5000_acc.txt"

so_luong = 5000

try:
    with open(input_file, "rb") as f_in:
        with open(output_file, "wb") as f_out:
            count = 0

            for line in f_in:
                if count >= so_luong:
                    break

                f_out.write(line)
                count += 1

    print("")
    print("Da lay:", count, "dong")
    print("File moi:", output_file)

except Exception as e:
    print("Loi:", e)

input("Nhan Enter de thoat...")
