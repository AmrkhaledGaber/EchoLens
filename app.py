import streamlit as st

# New Team Section Design
st.markdown('<div class="content-container">', unsafe_allow_html=True)

st.markdown("""
<h1 style="text-align: center; margin-bottom: 40px;">Meet Our Team</h1>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 30px; justify-items: center;">

  <div class="team-card">
    <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/mohamed_elsmawy.png" class="team-avatar">
    <h3>Mohamed ElSmawy</h3>
    <p>AIS</p>
  </div>

  <div class="team-card">
    <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/george_nashaat.png" class="team-avatar">
    <h3>George Nashaat</h3>
    <p>AIS</p>
  </div>

  <div class="team-card">
    <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/aya_tamer.png" class="team-avatar">
    <h3>Aya Tamer (Leader)</h3>
    <p>AIS</p>
  </div>

  <div class="team-card">
    <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/ahmed_dawood.png" class="team-avatar">
    <h3>Ahmed Dawood</h3>
    <p>AIS</p>
  </div>

  <div class="team-card">
    <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/amr_khaled.png" class="team-avatar">
    <h3>Amr Khaled</h3>
    <p>AIS</p>
  </div>

</div>

<style>
.team-card {
  background: linear-gradient(135deg, #2a2a2a, #1e1e1e);
  padding: 20px;
  border-radius: 15px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0,0,0,0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid #FF4B4B;
  width: 100%;
  max-width: 250px;
}

.team-card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 30px rgba(255, 75, 75, 0.4);
}

.team-avatar {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 50%;
  margin-bottom: 15px;
  border: 2px solid #FF4B4B;
}

.team-card h3 {
  color: #FF4B4B;
  margin: 10px 0 5px;
}

.team-card p {
  color: #ccc;
  font-size: 14px;
  margin: 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
