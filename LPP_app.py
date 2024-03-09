from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("D:\\EDA\\LaptopPrice_Predictor v1.0\\LaptopPrice_Predictor.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("WebApp.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        
        # Brands
        brand = request.form['Brand']
        if (brand == 'ASUS'):
            ASUS = 1
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0

        elif (brand == 'Acer'):
            ASUS = 0
            Acer = 1
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0

        elif (brand == 'Apple'):
            ASUS = 0
            Acer = 0
            Apple = 1
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0
            
        elif (brand == 'CHUWI'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 1
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0
            
        elif (brand == 'DELL'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 1
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0
            
        elif (brand == 'GIGABYTE'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 1
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0 

        elif (brand == 'HP'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 1
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0

        elif (brand == 'Infinix'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 1
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0

        elif (brand == 'LG'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 1
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0

        elif (brand == 'Lenovo'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 1
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0
            
        elif (brand == 'MICROSOFT'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 1
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0
            
        elif (brand == 'MSI'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 1
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0
            
        elif (brand == 'Primebook'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 1
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0
            
        elif (brand == 'SAMSUNG'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 1
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0
            
        elif (brand == 'Ultimus'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 1
            WINGS = 0
            ZEBRONICS = 0
            realme = 0
            
        elif (brand == 'WINGS'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 1
            ZEBRONICS = 0
            realme = 0
            
        elif (brand == 'ZEBRONICS'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 1
            realme = 0
            
        elif (brand == 'realme'):
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 1

        else:
            ASUS = 0
            Acer = 0
            Apple = 0
            CHUWI = 0
            DELL = 0
            GIGABYTE = 0
            HP = 0
            Infinix = 0
            LG = 0
            Lenovo = 0
            MICROSOFT = 0
            MSI = 0
            Primebook = 0
            SAMSUNG = 0
            Ultimus = 0
            WINGS = 0
            ZEBRONICS = 0
            realme = 0
            
        # -------------------------------------------------------------
        # -------------------------------------------------------------
        # -------------------------------------------------------------
        # -------------------------------------------------------------           
            
        # Processors
        Source = request.form['Processor']
        if (Source == 'Core i3'):
            Core_i3 = 1
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'M1'):
            Core_i3 = 0
            M1 = 1
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Core i7'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 1
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Core i5'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 1
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Ryzen 5 Hexa Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 1
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Celeron Dual Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 1
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Ryzen 7 Octa Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 1
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Ryzen 5 Quad Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 1
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Ryzen 3 Dual Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 1
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Ryzen 3 Quad Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 1
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'M2'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 1
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Celeron Quad Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 1
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Athlon Dual Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 1
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'MediaTek Kompanio 1200'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 1
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Rygen 9 Octa Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 1
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'MediaTek MT8788'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 1
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Ryzen Z1 HexaCore'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 1
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'MediaTek Kompanio 500'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 1
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Core i9'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 1
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'MediaTek Kompanio 520'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 1
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Ryzen Z1 Octa Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 1
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Pentium Silver'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 1
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Ryzen 5'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 1
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'M1 Max'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 1
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'M2 Max'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 1
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'M3 Pro'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 1
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'M1 Pro'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 1
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Ryzen 7 Quad Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 1
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Ryzen 5 Dual Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 1
            Ryzen_9_16_Core = 0
            
        elif (Source == 'Ryzen 9 16 Core'):
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 1
            
        else:
            Core_i3 = 0
            M1 = 0
            Core_i7 = 0
            Core_i5 = 0
            Ryzen_5_Hexa_Core = 0
            Celeron_Dual_Core = 0
            Ryzen_7_Octa_Core = 0
            Ryzen_5_Quad_Core = 0
            Ryzen_3_Dual_Core = 0
            Ryzen_3_Quad_Core = 0
            M2 = 0
            Celeron_Quad_Core = 0
            Athlon_Dual_Core = 0
            MediaTek_Kompanio_1200 = 0
            Ryzen_9_Octa_Core = 0
            MediaTek_MT8788 = 0
            Ryzen_Z1_HexaCore = 0
            MediaTek_Kompanio_500 = 0
            Core_i9 = 0
            MediaTek_Kompanio_520 = 0
            Ryzen_Z1_Octa_Core = 0
            Pentium_Silver = 0
            Ryzen_5 = 0
            M1_Max = 0
            M2_Max = 0
            M3_Pro = 0
            M1_Pro = 0
            Ryzen_7_Quad_Core = 0
            Ryzen_5_Dual_Core = 0
            Ryzen_9_16_Core = 0
            
        # -------------------------------------------------------------
        # -------------------------------------------------------------
        # -------------------------------------------------------------
        # -------------------------------------------------------------           
            
        # Operating System
        Source = request.form["Operating System"]
        if (Source == 'Windows 11 Home'):
            Windows_11_Home = 1
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0
            
        elif (Source == 'Mac OS Big Sur'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 1
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0

        elif (Source == 'DOS'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 1
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0

        elif (Source == 'Mac OS Monterey'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 1
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0

        elif (Source == 'Chrome'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 1
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0

        elif (Source == 'Windows 10'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 1
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0

        elif (Source == 'Windows 10 Home'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 1
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0
            
        elif (Source == 'Prime OS'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 1
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0
            
        elif (Source == 'Windows 11 Pro'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 1
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0
            
        elif (Source == 'Ubuntu'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 1
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0
            
        elif (Source == 'Windows 10 Pro'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 1
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0
            
        elif (Source == 'macOS Ventura'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 1
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0
            
        elif (Source == 'macOS Sonoma'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 1
            Mac_OS_Mojave = 0
            
        elif (Source == 'Mac OS Mojave'):
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 1
            
        else:
            Windows_11_Home = 0
            Mac_OS_Big_Sur = 0
            DOS = 0
            Mac_OS_Monterey = 0
            Chrome = 0
            Windows_10 = 0
            Windows_10_Home = 0
            Prime_OS = 0
            Windows_11_Pro = 0
            Ubuntu = 0
            Windows_10_Pro = 0
            macOS_Ventura = 0
            macOS_Sonoma = 0
            Mac_OS_Mojave = 0
            
        # -------------------------------------------------------------
        # -------------------------------------------------------------
        # -------------------------------------------------------------
        # -------------------------------------------------------------           
            
        # Storage
        Source = request.form["Storage"]
        if (Source == '512 GB'):
            s_512_GB = 1
            s_256_GB = 0
            s_1_TB = 0
            s_2_TB = 0
            s_4_TB = 0
            s_128_GB = 0
            s_64_GB = 0
            s_3_TB = 0
            s_6_TB = 0
            
        elif (Source == '256 GB'):
            s_512_GB = 0
            s_256_GB = 1
            s_1_TB = 0
            s_2_TB = 0
            s_4_TB = 0
            s_128_GB = 0
            s_64_GB = 0
            s_3_TB = 0
            s_6_TB = 0
            
        elif (Source == '1 TB'):
            s_512_GB = 0
            s_256_GB = 0
            s_1_TB = 1
            s_2_TB = 0
            s_4_TB = 0
            s_128_GB = 0
            s_64_GB = 0
            s_3_TB = 0
            s_6_TB = 0
            
        elif (Source == '2 TB'):
            s_512_GB = 0
            s_256_GB = 0
            s_1_TB = 0
            s_2_TB = 1
            s_4_TB = 0
            s_128_GB = 0
            s_64_GB = 0
            s_3_TB = 0
            s_6_TB = 0
            
        elif (Source == '4 TB'):
            s_512_GB = 0
            s_256_GB = 0
            s_1_TB = 0
            s_2_TB = 0
            s_4_TB = 1
            s_128_GB = 0
            s_64_GB = 0
            s_3_TB = 0
            s_6_TB = 0
            
        elif (Source == '128 GB'):
            s_512_GB = 0
            s_256_GB = 0
            s_1_TB = 0
            s_2_TB = 0
            s_4_TB = 0
            s_128_GB = 1
            s_64_GB = 0
            s_3_TB = 0
            s_6_TB = 0
            
        elif (Source == '64 GB'):
            s_512_GB = 0
            s_256_GB = 0
            s_1_TB = 0
            s_2_TB = 0
            s_4_TB = 0
            s_128_GB = 0
            s_64_GB = 1
            s_3_TB = 0
            s_6_TB = 0
            
        elif (Source == '3 TB'):
            s_512_GB = 0
            s_256_GB = 0
            s_1_TB = 0
            s_2_TB = 0
            s_4_TB = 0
            s_128_GB = 0
            s_64_GB = 0
            s_3_TB = 1
            s_6_TB = 0
            
        elif (Source == '6 TB'):
            s_512_GB = 0
            s_256_GB = 0
            s_1_TB = 0
            s_2_TB = 0
            s_4_TB = 0
            s_128_GB = 0
            s_64_GB = 0
            s_3_TB = 0
            s_6_TB = 1
            
        else:
            s_512_GB = 0
            s_256_GB = 0
            s_1_TB = 0
            s_2_TB = 0
            s_4_TB = 0
            s_128_GB = 0
            s_64_GB = 0
            s_3_TB = 0
            s_6_TB = 0
            
        # -------------------------------------------------------------
        # -------------------------------------------------------------
        # -------------------------------------------------------------
        # -------------------------------------------------------------           
            
        # RAM
        Source = request.form["RAM"]
        if (Source == '8 GB'):
            r_8_GB = 1
            r_16_GB = 0
            r_4_GB = 0
            r_12_GB = 0
            r_32_GB = 0
            r_64_GB = 0
            r_18_GB = 0
            
        elif (Source == '16 GB'):
            r_8_GB = 0
            r_16_GB = 1
            r_4_GB = 0
            r_12_GB = 0
            r_32_GB = 0
            r_64_GB = 0
            r_18_GB = 0
            
        elif (Source == '4 GB'):
            r_8_GB = 0
            r_16_GB = 0
            r_4_GB = 1
            r_12_GB = 0
            r_32_GB = 0
            r_64_GB = 0
            r_18_GB = 0
            
        elif (Source == '12 GB'):
            r_8_GB = 0
            r_16_GB = 0
            r_4_GB = 0
            r_12_GB = 1
            r_32_GB = 0
            r_64_GB = 0
            r_18_GB = 0
            
        elif (Source == '32 GB'):
            r_8_GB = 0
            r_16_GB = 0
            r_4_GB = 0
            r_12_GB = 0
            r_32_GB = 1
            r_64_GB = 0
            r_18_GB = 0
            
        elif (Source == '64 GB'):
            r_8_GB = 0
            r_16_GB = 0
            r_4_GB = 0
            r_12_GB = 0
            r_32_GB = 0
            r_64_GB = 1
            r_18_GB = 0
            
        elif (Source == '18 GB'):
            r_8_GB = 0
            r_16_GB = 0
            r_4_GB = 0
            r_12_GB = 0
            r_32_GB = 0
            r_64_GB = 0
            r_18_GB = 1
            
        else:
            r_8_GB = 0
            r_16_GB = 0
            r_4_GB = 0
            r_12_GB = 0
            r_32_GB = 0
            r_64_GB = 0
            r_18_GB = 0
            
        # -------------------------------------------------------------
        # -------------------------------------------------------------
        # -------------------------------------------------------------
        # -------------------------------------------------------------           
            
        # Touch Screen
        Source = request.form["Touch Screen"]
        if (Source == 'No'):
            No = 1
            Yes = 0
            
        elif (Source == 'Yes'):
            No = 0
            Yes = 1
            
        else:
            No = 0
            Yes = 0
        
        prediction=model.predict([[
            HP ,
            Apple ,
            Lenovo ,
            ASUS ,
            DELL ,
            Acer ,
            SAMSUNG ,
            MSI ,
            Infinix ,
            Ultimus ,
            CHUWI ,
            WINGS ,
            ZEBRONICS ,
            Primebook ,
            GIGABYTE ,
            realme ,
            MICROSOFT ,
            LG ,
            Core_i3 ,
            M1 ,
            Core_i7 ,
            Core_i5 ,
            Ryzen_5_Hexa_Core ,
            Celeron_Dual_Core ,
            Ryzen_7_Octa_Core ,
            Ryzen_5_Quad_Core ,
            Ryzen_3_Dual_Core ,
            Ryzen_3_Quad_Core ,
            M2 ,
            Celeron_Quad_Core ,
            Athlon_Dual_Core ,
            MediaTek_Kompanio_1200 ,
            Ryzen_9_Octa_Core ,
            MediaTek_MT8788 ,
            Ryzen_Z1_HexaCore ,
            MediaTek_Kompanio_500 ,
            Core_i9 ,
            MediaTek_Kompanio_520 ,
            Ryzen_Z1_Octa_Core ,
            Pentium_Silver ,
            Ryzen_5 ,
            M1_Max ,
            M2_Max ,
            M3_Pro ,
            M1_Pro ,
            Ryzen_7_Quad_Core ,
            Ryzen_5_Dual_Core ,
            Ryzen_9_16_Core ,
            Windows_11_Home ,
            Mac_OS_Big_Sur ,
            DOS ,
            Mac_OS_Monterey ,
            Chrome ,
            Windows_10 ,
            Windows_10_Home ,
            Prime_OS ,
            Windows_11_Pro ,
            Ubuntu ,
            Windows_10_Pro ,
            macOS_Ventura ,
            macOS_Sonoma ,
            Mac_OS_Mojave ,
            s_512_GB ,
            s_256_GB ,
            s_1_TB ,
            s_2_TB ,
            s_4_TB ,
            s_128_GB ,
            s_64_GB ,
            s_3_TB ,
            s_6_TB ,
            r_8_GB ,
            r_16_GB ,
            r_4_GB ,
            r_12_GB ,
            r_32_GB ,
            r_64_GB ,
            r_18_GB ,
            No ,
            Yes
        ]])

        output=round(prediction[0],2)

        return render_template('WebApp.html',prediction_text="Your Laptop price is Rs. {}".format(output))


    return render_template("WebApp.html")




if __name__ == "__main__":
    app.run(debug=True)
