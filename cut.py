input_file = input("Nhap duong dan file: ").strip().strip('"')
output_file = "5000_acc.txt"

so_luong = 5000

with open(input_file, "r") as f_in:
    with open(output_file, "w") as f_out:
        for i, line in enumerate(f_in):
            if i >= so_luong:
                break
            f_out.write(line)

print("Da lay 5000 acc!")
print("File moi:", output_file)

input("Nhan Enter de thoat...")
