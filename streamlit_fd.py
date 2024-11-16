import streamlit as st
import torch
import pickle
import numpy as np

# Load model and scaler
model = torch.load('final_model.pth', map_location=torch.device('cpu'))
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Set up the page
st.set_page_config(
    page_title="FINANCIAL DISTRESS ANALYSIS",
    page_icon="📉",
    layout="wide"
)

# Main title with enhanced styling
st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        color: #333333;
        font-family: 'Poppins', sans-serif;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    </style>
    <h1 class="main-title">Financial Distress Prediction Dashboard</h1>
    """, unsafe_allow_html=True)

# Sidebar with custom styling
st.sidebar.header("📊 Financial Distress Dashboard")
selected = st.sidebar.selectbox(
    label="Navigate",
    options=["Home", "Profil Creator", "Terms and Conditions", "Prediction"],  # Added "Profil Creator"
    help="Choose a section to navigate."
)

# Sidebar styling CSS
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content h2 {
        color: #333;
        font-family: 'Poppins', sans-serif;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Gradient background for main content
st.markdown("""
    <style>
    .reportview-container {
        background: linear-gradient(to right, #76c893, #ffde59);
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# Home Section
if selected == "Home":
    st.markdown(
        """
        <style>
        .moving-text {
            display: inline-block;
            font-size: 24px;
            color: #333;
            animation: moveText 10s linear infinite;
            margin-top: 5px;
        }

        @keyframes moveText {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
                .centered-image {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        </style>
        
        <div style="text-align: center;">
            <span class="moving-text">Welcome to the Financial Distress Analysis Application!</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h4 style='text-align: center;'>This Dashboard Provides Tools to Predict Financial Distress Risk</h4>", unsafe_allow_html=True)
    st.image("fd.png", width=800)

# Profil Creator Section
# Profil Creator Section
elif selected == "Profil Creator":
    st.markdown("""
        <style>
        .profil-title {
            font-size: 30px;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin-top: 5px;
            margin-bottom: 20px;
            font-family: 'Poppins', sans-serif;
        }
        .profil-content {
            font-size: 18px;
            line-height: 1.6;
            color: #333;
            font-family: 'Poppins', sans-serif;
            padding-top: 35px; /* Mengatur jarak dari atas agar lebih tengah */
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<h2 class="profil-title">Profil Creator</h2>', unsafe_allow_html=True)

    # Using st.columns to place the image and text side by side
    col1, col2 = st.columns([1, 3])  # Adjust the width ratio as needed for better alignment

    with col1:
        st.image("fotoku hd.png", width=180)  # Ensure fotoku.png is in the same directory

    with col2:
        st.markdown("""
            <div class="profil-content">
                <p><strong>Nama:</strong> Ni Luh Eva Pradnyaningsih</p>
                <p><strong>NRP:</strong> 2043211106</p>
                <p><strong>Jurusan:</strong> Statistika Bisnis</p>
                <p><strong>Universitas:</strong> Institut Teknologi Sepuluh Nopember</p>
                <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/evapradnyaningsih" target="_blank">LinkedIn - Ni Luh Eva Pradnyaningsih</a></p>
            </div>
        """, unsafe_allow_html=True)

# Cara Menggunakan Section
elif selected == "Terms and Conditions":
    st.markdown("""
        <style>
        .cara-menggunakan-title {
            font-size: 30px;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
            font-family: 'Poppins', sans-serif;
        }
        .cara-menggunakan-content {
            font-size: 18px;
            line-height: 1.6;
            color: #333;
            text-align: justify;
            margin: 0 auto;
            width: 80%;
            font-family: 'Poppins', sans-serif;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<h2 class="cara-menggunakan-title">Cara Menggunakan Dashboard</h2>', unsafe_allow_html=True)

    st.markdown("""
        <div class="cara-menggunakan-content">
        <p>Ikuti panduan berikut untuk menggunakan dashboard prediksi financial distress ini dengan efektif:</p>
        <ol>
            <li><strong>Memasukkan Data:</strong> Masukkan nilai-nilai keuangan perusahaan pada kolom yang tersedia di bagian <em>Prediction</em>. Pastikan untuk memasukkan data numerik dengan menggunakan titik sebagai pemisah desimal (contoh: 1.5).</li>
            <li><strong>Pastikan Data Valid:</strong> Pastikan semua kolom telah terisi sebelum menekan tombol <em>Test Prediction</em>. Setiap kolom mewakili metrik keuangan seperti ROA, DAR, CR, dll., yang digunakan model untuk menentukan kategori perusahaan.</li>
            <li><strong>Hasil Prediksi:</strong> Setelah menekan tombol <em>Test Prediction</em>, dashboard akan menampilkan hasil prediksi sebagai <span style="color:green;">"Non-Distress"</span> atau <span style="color:red;">"Distress"</span>. <span style="color:green;">Non-Distress</span> berarti perusahaan berada dalam kategori aman, sedangkan <span style="color:red;">Distress</span> berarti perusahaan berada dalam risiko keuangan.</li>
        </ol>
        <p>Pastikan untuk selalu menggunakan data yang terbaru dan valid agar prediksi yang dihasilkan lebih akurat.</p>
        </div>
        """, unsafe_allow_html=True)

# Prediction Section
elif selected == "Prediction":
    st.markdown("""
        <style>
        .prediction-title {
            font-size: 30px;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin-bottom: 25px;
            font-family: 'Poppins', sans-serif;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            padding: 10px 50px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        </style>
        """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="prediction-title">Prediction Section</h1>', unsafe_allow_html=True)

    # Input fields with a cleaner layout
    col1, col2 = st.columns(2)
    with col1:
        ROA = st.text_input('Return on Assets (ROA) (kali)')
        DAR = st.text_input('Debt to Assets Ratio (DAR) (kali)')
        CR = st.text_input('Current Ratio (CR) (kali)')
        QR = st.text_input('Quick Ratio (QR) (kali)')
        Cash_Ratio = st.text_input('Cash Ratio (kali)')
        DER = st.text_input('Debt to Equity Ratio (DER) (kali)')
    with col2:
        Equity_Multiplier = st.text_input('Equity Multiplier (kali)')
        ROE = st.text_input('Return on Equity (ROE) (kali)')
        Total_Assets_Turnover = st.text_input('Total Assets Turnover (kali)')
        PER = st.text_input('Price to Earnings Ratio (PER) (kali)')
        PBV = st.text_input('Price to Book Value Ratio (PBV) (kali)')

    # Prediction button and result
    fd_deteksi = ''
    if st.button('Test Prediction'):
        try:
            # Convert inputs to a list of floats and reshape for scaler
            input_data = np.array([[float(ROA), float(DAR), float(CR), float(QR), float(Cash_Ratio), 
                                    float(DER), float(Equity_Multiplier), float(ROE), 
                                    float(Total_Assets_Turnover), float(PER), float(PBV)]])
            # Normalize input using the loaded scaler
            input_scaled = scaler.transform(input_data)

            # Convert the scaled input to a PyTorch tensor
            input_tensor = torch.FloatTensor(input_scaled)

            # Make a prediction
            model.eval()
            with torch.no_grad():
                output = model(input_tensor)
                fd_prediction = (output > 0.5).int()

            # Display the result with color-coded messages
            if fd_prediction[0].item() == 1:
                fd_deteksi = '<div style="text-align:center; background-color:#f8d7da; color:#721c24; padding:10px; border-radius:5px; font-size:20px;">⚠️ <strong>Distress</strong>: The company is in a category of financial distress.</div>'
            else:
                fd_deteksi = '<div style="text-align:center; background-color:#d4edda; color:#155724; padding:10px; border-radius:5px; font-size:20px;">✅ <strong>Non-Distress</strong>: The company is in a category of non-distress.</div>'
        
        except ValueError as ve:
            st.error(f'Value Error: {ve}')
        except IndexError as ie:
            st.error(f'Index Error: {ie}')
        except Exception as e:
            st.error(f'An error occurred: {e}')

    # Display the styled prediction result
    if fd_deteksi:
        st.markdown(fd_deteksi, unsafe_allow_html=True)
