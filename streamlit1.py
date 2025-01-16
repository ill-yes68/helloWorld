import streamlit as st
import seaborn as sns

# Chargement des données taxis depuis Seaborn
data = sns.load_dataset('taxis')

# Définition des images pour chaque arrondissement avec les nouvelles URLs
arrondissement_images = {
    "Manhattan": "https://img.andrewprokos.com/MIDTOWN-MANHATTAN-PANORAMIC-SKYLINE-LONG-EXPOSURE-COLOR-3083-1100PX-500x208@2x.jpg",
    "Brooklyn": "https://img.pikbest.com/ai/illus_our/20230424/86245c1e90a5b339ddca19f0beba1acf.jpg!w700wp",
    "Queens": "https://images.ctfassets.net/1aemqu6a6t65/4hQFNm7rQvHHKaPjsx2FZ0/174e4cf2006c9876fec57b46b0ea98b1/PS1-Long_Island_CIty-Queens-NYC-Photo-.jpg",
    "Bronx": "https://previews.123rf.com/images/melpomen/melpomen2003/melpomen200300083/141274538-vue-a%C3%A9rienne-du-bronx-new-york-city.jpg",
    "Staten Island": "https://cdn.vox-cdn.com/thumbor/8lRhbtdwqFxYhHsHZAwbbKuFB2c=/0x0:2000x1328/1200x800/filters:focal(840x504:1160x824)/cdn.vox-cdn.com/uploads/chorus_image/image/54582755/111028_15_57_58_DSC_0199.0.jpg"
}
# Titre principal de l'application
st.title("Bienvenue sur le site web de Illyes")

# Création du menu déroulant pour sélectionner un arrondissement
arrondissement = st.selectbox(
    "Indiquez votre arrondissement de récupération",
    list(arrondissement_images.keys())
)

# Affichage du choix de l'utilisateur
st.write(f"Tu as choisi : {arrondissement}")

# Affichage de l'image correspondant à l'arrondissement
image_url = arrondissement_images[arrondissement]
st.image(image_url, caption=f"{arrondissement}", use_container_width=True)
