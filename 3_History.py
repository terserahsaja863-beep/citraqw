import streamlit as st

from src.state import configure_logging, initialize_session_state
from src.ui import configure_page, empty_scanner_state, metric_card, render_header, render_sidebar


configure_logging()
configure_page("History | Smart Document Scanner")
render_sidebar()
initialize_session_state()
render_header("History", "Track document scans and recent activity")

history = st.session_state.history

cols = st.columns(3)
with cols[0]:
    metric_card("Today", str(len(history)), "Scans in current session")
with cols[1]:
    metric_card("This Week", str(len(history)), "Session memory history")
with cols[2]:
    metric_card("Exports", str(st.session_state.exports_count), "JPG/PDF downloads")

st.write("")
st.markdown('<div class="glass-card"><div class="panel-title">Recent Documents</div><div class="soft-note">Riwayat disimpan selama sesi Streamlit berjalan.</div></div>', unsafe_allow_html=True)

if not history:
    st.write("")
    empty_scanner_state("Belum ada history", "Scan atau enhance dokumen terlebih dahulu untuk mengisi riwayat.")
else:
    st.dataframe(history, use_container_width=True, hide_index=True)
    st.write("")
    for item in history[:5]:
        st.markdown(
            f"""
            <div class="filter-pill">
                📄 {item["Nama File"]} · {item["Mode Scan"]} · {item["Resolusi"]} · {item["Processing Time"]}
            </div>
            """,
            unsafe_allow_html=True,
        )
