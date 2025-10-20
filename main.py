import streamlit as st

st.title("Çağrı Güngör")

bordro=st.checkbox("Bordro")
gelir=st.number_input("Brüt Yıllık Gelirinizi Giriniz")

v158=158000*0.15
v330=(330000-158000)*0.20
v1200=(1200000-330000)*0.27
v4300=(4300000-1200000)*0.35
v800=(800000-330000)*0.27
v4300x=(4300000-800000)*0.35

if bordro:
    if gelir<158000:
        vergi=gelir*0.15
    elif gelir<330000:
        vergi=v158+((gelir-158000)*0.20)
    elif gelir<1200000:
        vergi=v158+v330+((gelir-330000)*0.27)
    elif gelir<4300000:
        vergi=v158+v330+v1200+((gelir-1200000)*0.35)
    else:
        vergi=v158+v330+v1200+v4300+((gelir-4300000)*0.40)
else:
    if gelir<158000:
        vergi=gelir*0.15
    elif gelir<330000:
        vergi=v158+((gelir-158000)*0.20)
    elif gelir<800000:
        vergi=v158+v330+((gelir-330000)*0.27)
    elif gelir<4300000:
        vergi=v158+v330+v800+((gelir-800000)*0.35)
    else:
        vergi=v158+v330+v800+v4300x+((gelir-4300000)*0.40)

net=gelir-vergi
ay=gelir/12
aynet=net/12

st.write("Yıllık Gelir",gelir,
         "Yıllık Net Gelir",net,
         "Aylık Brüt Gelir",round(ay,2),"Aylık Net Gelir",
         round(aynet,2),"Toplam Vergi",vergi)


# streamlit run main.py
