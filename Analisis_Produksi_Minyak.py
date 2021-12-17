"""
NAMA : Prima Adi Putra
NIM : 12220124
UAS PROKOM
"""
#mengimport Modul yang di butuhkan==========
import json
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
#===================================


#Open file========================================================================================
buka = open("kode_negara_lengkap.json") 
file_json = json.load(buka)
csv_data = pd.read_csv("produksi_minyak_mentah.csv")
json_data = pd.DataFrame.from_dict(file_json, orient = 'columns')

st.set_page_config(page_title='tes streamlit',
                   layout='wide', page_icon=':oil_drum:')

st.markdown( "## Aplikasi Sederhana Analisis Minyak Mentah ")
#=================================================================================================


#=============================== SOAL NOMOR 1 =========================================================================
st.markdown( "## Grafik Hubungan Antara Produksi Minyak dengan Waktu Pada Suatu Negara ")
X = st.text_input("Masukkan Kode negara: ")

list_a = []

for i in list(csv_data['kode_negara']):
    if i not in list(json_data['alpha-3']):
        list_a.append(i)

for i in list_a:
    csv_data = csv_data[csv_data.kode_negara != i]

list_country_name = []
data1 = csv_data.loc[csv_data['kode_negara'] == X]

data1.plot(x='tahun', y='produksi')
ax.set_facecolor("orange")
grafik1 = plt.show()
st.pyplot(grafik1)
#========================================================================================================================


#========================SOAL NOMOR 2====================================================================================
st.markdown( "## Grafik Negara Dengan Produksi Terbesar Pada Tahun Tertentu ")
list_tahun = []
#==========Pembuatan Select Box==========
for i in list(csv_data['tahun']):
    if i not in list_tahun:
        list_tahun.append(i)
T = st.selectbox("Masukkan tahun: ", list_tahun)
#========================================
#Pengubahan input menjadi integer========
T = int(T)
#========================================
B_terbesar = st.number_input("Masukkan banyak negara: ", min_value=1)
B_terbesar = int(B_terbesar)

data2 = csv_data.loc[csv_data['tahun'] == T]
data2 = data2.sort_values(by=['produksi'], ascending=False)
data3 = data2[:B_terbesar]

data3.plot.bar(x='kode_negara', y='produksi')
grafik = plt.show()
st.pyplot(grafik)
#===============================================================================================================================


#==============================SOAL NOMOR 3=====================================================================================
st.markdown( "## Grafik Negara Dengan Produksi Kumulatif Terbesar  ")
#Pembuatan List=====================================================
count = []
list_count = []
#===================================================================
#Input banyak negara yg diinginkan==================================
B_kumulatif = st.number_input("Masukkan banyak negara: ", min_value=1, key = "B_kumulatif")
#mengubah menjadi integer=============
B_kumulatif = int(B_kumulatif)
#===================================
for x in list(csv_data['kode_negara']):
    if x not in list_count:
        list_count.append(x)

for y in list_count:
    a = csv_data.loc[csv_data['kode_negara'] == y, 'produksi'].sum()
    count.append(a)

data_count = pd.DataFrame(list(zip(list_count, count)), columns=['kode_negara', 'kumulatif'])
data_count = data_count.sort_values(by=['kumulatif'], ascending=False)
data_count1 = data_count[:B_kumulatif] 

#Pembuatan Grafik===================================================
data_count1.plot.bar(x='kode_negara', y='kumulatif')
grafik3 = plt.show()
st.pyplot(grafik3)
#============================================================================================================================



#==========================SOAL NOMOR 4===========================================================================================
#======================JUMLAH PRODUKSI TERBESAR======================
production_value = data2[:1].iloc[0]['produksi']
kode_negara = data2[:1].iloc[0]['kode_negara']
country_name = ""
country_region = ""
country_subregion = ""

for x in range(len(json_data)):
    if list(json_data['alpha-3'])[x] == kode_negara:
        country_name = list(json_data['name'])[x]
        country_region = list(json_data['region'])[x]
        country_subregion = list(json_data['sub-region'])[x]

col1, col2 = st.columns(2)
with col1:
    st.markdown( "## Negara Yang Memiliki Jumlah Produksi Minyak Mentah Terbesar Pada Tahun {}".format(T))
    st.text("{} \n{} \n{} \n{} \n{}".format(production_value, kode_negara, country_name, country_region, country_subregion))

production_value = data_count[:1].iloc[0]['kumulatif']
kode_negara = data_count[:1].iloc[0]['kode_negara']
country_name = ""
country_region = ""
country_subregion = ""

for m in range(len(json_data)):
    if list(json_data['alpha-3'])[m] == kode_negara:
        country_name = list(json_data['name'])[m]
        country_region = list(json_data['region'])[m]
        country_subregion = list(json_data['sub-region'])[m]

with col2:
    st.markdown("## Negara Yang Memiliki Jumlah Produksi Minyak Mentah Terbesar ")
    st.text("{} \n{} \n{} \n{} \n{}".format(production_value, kode_negara, country_name, country_region, country_subregion))


#================JUMLAH PRODUKSI TERKECIL========================================
smallest_data = data2[data2.produksi != 0]
smallest_data = smallest_data.sort_values(by=['produksi'], ascending=True)

production_value = smallest_data[:1].iloc[0]['produksi']
kode_negara = smallest_data[:1].iloc[0]['kode_negara']
country_name = ""
country_region = ""
country_subregion = ""

for p in range(len(json_data)):
    if list(json_data['alpha-3'])[p] == kode_negara:
        country_name = list(json_data['name'])[p]
        country_region = list(json_data['region'])[p]
        country_subregion = list(json_data['sub-region'])[p]

st.markdown("## Negara Yang Memiliki Produksi Minyak Mentah Terkecil Pada Tahun {}".format(T))
st.text("{} \n{} \n{} \n{} \n{}".format(production_value, kode_negara, country_name, country_region, country_subregion))

data_countmin = data_count[data_count.kumulatif != 0]
data_countmin = data_countmin.sort_values(by=['kumulatif'], ascending=True)

production_value = data_countmin[:1].iloc[0]['kumulatif']
kode_negara = data_countmin[:1].iloc[0]['kode_negara']
country_name = ""
country_region = ""
country_subregion = ""

for x in range(len(json_data)):
    if list(json_data['alpha-3'])[x] == kode_negara:
        country_name = list(json_data['name'])[x]
        country_region = list(json_data['region'])[x]
        country_subregion = list(json_data['sub-region'])[x]

st.markdown( "## Negara Yang Memiliki Produksi Minyak Mentah Terkecil ")
st.text("{} \n{} \n{} \n{} \n{}".format(production_value, kode_negara, country_name, country_region, country_subregion))

#==========================================PRODUKSI NOL==============================
st.markdown("## Negara Yang Memiliki Jumlah Produksi Minyak Mentah Nol ")
data_zero = data2[data2.produksi == 0]
zero_country_list = []
zero_region_list = []
zero_subregion_list = []

for x in range(len(data_zero)):
    for y in range(len(json_data)):
        if list(data_zero['kode_negara'])[x] == list(json_data['alpha-3'])[y]:
            zero_country_list.append(list(json_data['name'])[y])
            zero_region_list.append(list(json_data['region'])[y])
            zero_subregion_list.append(list(json_data['sub-region'])[y])

data_zero['negara'] = zero_country_list
data_zero['region'] = zero_region_list
data_zero['sub-region'] = zero_subregion_list

data_countnol = data_count[data_count.kumulatif == 0]
zero_count_country_list = []
zero_count_region_list = []
zero_count_subregion_list = []

for x in range(len(data_countnol)):
    for y in range(len(json_data)):
        if list(data_countnol['kode_negara'])[x] == list(json_data['alpha-3'])[y]:
            zero_count_country_list.append(list(json_data['name'])[y])
            zero_count_region_list.append(list(json_data['region'])[y])
            zero_count_subregion_list.append(list(json_data['sub-region'])[y])

data_countnol['negara'] = zero_count_country_list
data_countnol['region'] = zero_count_region_list
data_countnol['sub-region'] = zero_count_subregion_list

#====================Menampilkan di streamlit=======================
st.dataframe(data_zero)
st.table(data_countnol)

#Menghilangkan Warning di Streamlit======================
st.set_option('deprecation.showPyplotGlobalUse', False)

#================================APLIKASI SELESAI===========================================================
