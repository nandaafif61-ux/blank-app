import streamlit as st
import math

st.title("📐 Kalkulator Lengkap - Streamlit")

menu = st.sidebar.selectbox(
    "Pilih jenis perhitungan",
    [
        "Perhitungan Dasar",
        "Lingkaran",
        "Segitiga",
        "Persegi",
        "Persegi Panjang",
        "Kuadrat / Akar Kuadrat"
    ]
)

# -------------------------------
# PERHITUNGAN DASAR
# -------------------------------
if menu == "Perhitungan Dasar":
    st.header("➕ Perhitungan Dasar")

    a = st.number_input("Masukkan angka pertama:", value=0.0)
    b = st.number_input("Masukkan angka kedua:", value=0.0)

    operasi = st.selectbox("Pilih operasi", ["Tambah", "Kurang", "Kali", "Bagi"])

    if operasi == "Tambah":
        hasil = a + b
    elif operasi == "Kurang":
        hasil = a - b
    elif operasi == "Kali":
        hasil = a * b
    else:
        hasil = "Tidak bisa membagi dengan nol!" if b == 0 else a / b

    st.success(f"Hasil: {hasil}")


# -------------------------------
# LINGKARAN
# -------------------------------
elif menu == "Lingkaran":
    st.header("⚪ Perhitungan Lingkaran")

    r = st.number_input("Masukkan jari-jari (r):", value=0.0)

    luas = math.pi * r * r
    keliling = 2 * math.pi * r

    st.write(f"📏 Luas: {luas:.2f}")
    st.write(f"📏 Keliling: {keliling:.2f}")


# -------------------------------
# SEGITIGA
# -------------------------------
elif menu == "Segitiga":
    st.header("🔺 Perhitungan Segitiga")

    alas = st.number_input("Masukkan alas:", value=0.0)
    tinggi = st.number_input("Masukkan tinggi:", value=0.0)

    luas = 0.5 * alas * tinggi
    st.write(f"📏 Luas Segitiga: {luas}")


# -------------------------------
# PERSEGI
# -------------------------------
elif menu == "Persegi":
    st.header("⬛ Perhitungan Persegi")

    sisi = st.number_input("Masukkan panjang sisi:", value=0.0)

    luas = sisi * sisi
    keliling = 4 * sisi

    st.write(f"📏 Luas: {luas}")
    st.write(f"📏 Keliling: {keliling}")


# -------------------------------
# PERSEGI PANJANG
# -------------------------------
elif menu == "Persegi Panjang":
    st.header("▭ Perhitungan Persegi Panjang")

    p = st.number_input("Masukkan panjang:", value=0.0)
    l = st.number_input("Masukkan lebar:", value=0.0)

    luas = p * l
    keliling = 2 * (p + l)

    st.write(f"📏 Luas: {luas}")
    st.write(f"📏 Keliling: {keliling}")


# -------------------------------
# KUADRAT & AKAR KUADRAT
# -------------------------------
elif menu == "Kuadrat / Akar Kuadrat":
    st.header("√ Kuadrat & Akar")

    angka = st.number_input("Masukkan angka:", value=0.0)

    kuadrat = angka ** 2
    akar = math.sqrt(angka) if angka >= 0 else "Tidak bisa akar bilangan negatif"

    st.write(f"📏 Kuadrat: {kuadrat}")
    st.write(f"📏 Akar: {akar}")
