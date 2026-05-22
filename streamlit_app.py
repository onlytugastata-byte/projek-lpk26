import streamlit as st

st.title("🎈 Project Kelas D 2026")
import streamlit as st

st.title("🧮 Kalkulator Sederhana")

st.write("Masukkan dua angka, lalu pilih operasi hitung.")

angka1 = st.number_input("Masukkan angka pertama")
angka2 = st.number_input("Masukkan angka kedua")

operasi = st.selectbox(
    "Pilih operasi",
    ["Tambah", "Kurang", "Kali", "Bagi"]
)

if st.button("Hitung"):
    if operasi == "Tambah":
        hasil = angka1 + angka2
        st.success(f"Hasil: {angka1} + {angka2} = {hasil}")

    elif operasi == "Kurang":
        hasil = angka1 - angka2
        st.success(f"Hasil: {angka1} - {angka2} = {hasil}")

    elif operasi == "Kali":
        hasil = angka1 * angka2
        st.success(f"Hasil: {angka1} × {angka2} = {hasil}")

    elif operasi == "Bagi":
        if angka2 == 0:
            st.error("Tidak bisa dibagi dengan 0")
        else:
            hasil = angka1 / angka2
            st.success(f"Hasil: {angka1} ÷ {angka2} = {hasil}")
