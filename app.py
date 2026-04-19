import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Arup UK Projects | 2016–2018",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
[data-testid="stSidebar"] { background: #1a1a2e; }
[data-testid="stSidebar"] .stRadio label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] small { color: #e0e0e0 !important; }
[data-testid="stSidebar"] hr { border-color: #ffffff33; }
.project-header {
    padding: 1.6rem 2rem;
    border-radius: 12px;
    margin-bottom: 1.5rem;
    color: white;
}
.detail-box {
    background: #f8f9fa;
    border-radius: 8px;
    padding: 1.2rem;
    margin-top: 1rem;
    border-left: 5px solid;
}
.project-card {
    background: white;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 0.9rem 1rem;
    margin-bottom: 0.6rem;
    border-left: 5px solid;
}
</style>
""",
    unsafe_allow_html=True,
)

PROJECTS = [
    {
        "id": "cardiff_parkway",
        "name": "Cardiff Parkway",
        "subtitle": "Proposed New Railway Station",
        "location": "St Mellons, Cardiff, Wales",
        "coords": [51.5277, -3.1186],
        "type": "Rail",
        "color": "#4361EE",
        "years": "2016–2017",
        "brief": "Proposed new mainline station east of Cardiff at the M4/A48(M) junction, designed as a major park-and-ride transport interchange.",
        "description": (
            "Cardiff Parkway is a proposed new railway station on the South Wales Main Line, "
            "located at the Cardiff Gate junction east of the city centre. The scheme was designed "
            "to provide a 1,500-space park-and-ride, bus interchange, and direct rail services to "
            "Cardiff Central and Bristol, serving the growing communities of east Cardiff and the "
            "Vale of Glamorgan.\n\n"
            "At Arup (2016–2017), work focused on structural and civil engineering of the station "
            "platforms, footbridge, and access roads, alongside transport modelling for the catchment area."
        ),
        "status": "Pre-Construction",
        "status_color": "#4361EE",
        "status_detail": (
            "Planning permission was granted by Cardiff Council. The privately funded project, "
            "led by Cardiff Parkway Developments Ltd, continues to seek full investment commitment. "
            "As of 2024, the scheme remains in pre-construction phase with an updated design. "
            "If built, it would be one of the first new mainline stations in Wales in decades."
        ),
    },
    {
        "id": "gcre",
        "name": "Railway Test Track Wales",
        "subtitle": "Global Centre of Rail Excellence (GCRE)",
        "location": "Onllwyn, Neath Port Talbot, Wales",
        "coords": [51.7600, -3.7350],
        "type": "Rail Infrastructure",
        "color": "#E63946",
        "years": "2017–2018",
        "brief": "World-class railway testing and certification facility on a former open-cast mine site in the South Wales valleys.",
        "description": (
            "The Global Centre of Rail Excellence (GCRE) is one of the most ambitious rail infrastructure "
            "projects in UK history. Located on the former Nant Helen open-cast mine in the Dulais Valley, "
            "the facility is designed to provide a 7 km high-speed test loop, electrification testing "
            "infrastructure, and simulation facilities — enabling rolling stock and track systems to be "
            "certified without disrupting the operational network.\n\n"
            "Arup's work (2017–2018) covered early-stage civil engineering feasibility, geotechnical "
            "assessment of the former mining land, and options for the test track alignment and geometry."
        ),
        "status": "Under Construction",
        "status_color": "#F4A261",
        "status_detail": (
            "The GCRE secured joint funding from the UK Government and Welsh Government. "
            "Site enabling works and infrastructure development have progressed since 2022. "
            "The facility is expected to become operational from 2025–2026, with a 7 km high-speed loop "
            "and electrification test track. It will be one of Europe's premier rail testing centres, "
            "attracting rolling stock manufacturers from across the world."
        ),
    },
    {
        "id": "a30",
        "name": "A30 Chiverton to Carland Cross",
        "subtitle": "Trunk Road Dualling",
        "location": "Near Chiverton Cross, Cornwall",
        "coords": [50.2935, -5.0680],
        "type": "Highways",
        "color": "#2DC653",
        "years": "2016–2018",
        "brief": "Dualling of a critical 8-mile section of the A30 in Cornwall, one of the most dangerous trunk roads in the South West.",
        "description": (
            "The A30 Chiverton to Carland Cross scheme upgraded approximately 8 miles of single-carriageway "
            "A30 in mid-Cornwall to dual carriageway standard. This section was one of the most dangerous "
            "stretches of trunk road in South West England, with a high accident record and severe seasonal "
            "congestion — the main gateway to west Cornwall.\n\n"
            "Arup's work (2016–2018) covered detailed highway design, structures engineering for new "
            "bridges and underpasses, drainage design, and environmental assessment."
        ),
        "status": "Completed",
        "status_color": "#06D6A0",
        "status_detail": (
            "The Development Consent Order (DCO) was granted by the Planning Inspectorate in 2020. "
            "Construction commenced in 2022 and the scheme was substantially completed by late 2023 / "
            "early 2024. The new dual carriageway has significantly reduced journey times and accidents, "
            "and is widely regarded as a major economic enabler for west Cornwall."
        ),
    },
    {
        "id": "a303",
        "name": "A303 Stonehenge",
        "subtitle": "Dual Carriageway & Tunnel",
        "location": "Amesbury, Wiltshire",
        "coords": [51.1789, -1.8262],
        "type": "Highways / Tunnelling",
        "color": "#7B2D8B",
        "years": "2016–2018",
        "brief": "Scheme to dual the A303 near Stonehenge and tunnel beneath the UNESCO World Heritage Site, removing surface traffic from the landscape.",
        "description": (
            "The A303 Amesbury to Berwick Down scheme proposed upgrading approximately 8 miles of the A303 "
            "to dual carriageway, including a 3.3 km tunnel beneath the Stonehenge World Heritage Site. "
            "The tunnel would remove blighting surface traffic from the Stonehenge landscape and improve "
            "the A303 as the main route between London and the South West.\n\n"
            "Arup contributed to early design development including tunnel cross-section options, portal "
            "locations, ventilation strategy, and structural options for cut-and-cover sections."
        ),
        "status": "Planning Dispute",
        "status_color": "#FF6B6B",
        "status_detail": (
            "The project has been mired in controversy. The original DCO was rejected by the Planning "
            "Inspectorate in 2021 on grounds of harm to the World Heritage Site. National Highways "
            "resubmitted a revised application, but UNESCO, Historic England, and campaign groups continue "
            "to oppose it. As of 2024–2025, the scheme remains one of the most contested infrastructure "
            "projects in England, with ongoing legal battles and no confirmed construction date."
        ),
    },
    {
        "id": "m4_relief",
        "name": "M4 Relief Road",
        "subtitle": "Newport Motorway Bypass",
        "location": "Newport, South Wales",
        "coords": [51.5400, -2.9700],
        "type": "Motorway",
        "color": "#F77F00",
        "years": "2016–2018",
        "brief": "Proposed 23-mile motorway bypass south of Newport to relieve one of the most congested sections of motorway in the UK.",
        "description": (
            "The M4 Relief Road (M4 Corridor Around Newport) was a proposed 23-mile (37 km) new motorway "
            "running south of Newport to bypass the existing M4, which suffers severe congestion through "
            "the city. The scheme included a major crossing of the Usk estuary and traversed the Gwent "
            "Levels — a nationally important wetland SSSI.\n\n"
            "Arup's work (2016–2018) included detailed highway and structural engineering, geotechnical "
            "assessment of the Gwent Levels, and design of the major Usk crossing structure."
        ),
        "status": "Cancelled",
        "status_color": "#ADB5BD",
        "status_detail": (
            "In June 2019, Welsh Government First Minister Mark Drakeford cancelled the scheme following "
            "a public inquiry that concluded benefits did not justify the estimated £1.4 billion cost, "
            "and that environmental impact on the Gwent Levels SSSI was unacceptable. The decision was "
            "hugely controversial within the business and haulage community. The M4 through Newport "
            "remains one of the most congested motorways in the UK, and the Welsh Government has since "
            "pursued active travel and public transport improvements as an alternative."
        ),
    },
    {
        "id": "southsea",
        "name": "Southsea Coastal Defence",
        "subtitle": "Sea Defence Scheme",
        "location": "Southsea, Portsmouth",
        "coords": [50.7753, -1.0636],
        "type": "Coastal Engineering",
        "color": "#0077B6",
        "years": "2017–2018",
        "brief": "Major £105 million flood defence scheme protecting 10,000 properties in Southsea and Old Portsmouth from rising sea levels.",
        "description": (
            "The Southsea Coastal Defence scheme is one of the largest coastal defence projects in "
            "England, protecting over 10,000 homes and businesses from flooding caused by rising sea "
            "levels, storm surges, and increased wave heights along approximately 4.5 km of coastline "
            "between Eastney and Old Portsmouth.\n\n"
            "Arup's involvement (2017–2018) covered structural engineering of the new sea wall and "
            "promenade structures, rock armour design, beach management strategy, and drainage "
            "improvements along the Southsea seafront."
        ),
        "status": "Under Construction",
        "status_color": "#F4A261",
        "status_detail": (
            "The scheme received full funding approval from the Environment Agency and Portsmouth City "
            "Council. Construction commenced in 2021 across multiple phases. Significant sections of "
            "new sea wall, promenade, and beach management between Canoe Lake and Clarence Pier were "
            "completed in 2023–2024. The full scheme is expected to reach completion around 2026–2027, "
            "providing century-long protection against coastal flooding for Southsea and Old Portsmouth."
        ),
    },
]

STATUS_EMOJI = {
    "Completed": "✅",
    "Under Construction": "🚧",
    "Pre-Construction": "📋",
    "Cancelled": "❌",
    "Planning Dispute": "⚠️",
}


def popup_html(p: dict) -> str:
    sc = p["status_color"]
    emoji = STATUS_EMOJI.get(p["status"], "📍")
    preview = p["status_detail"][:200] + "…"
    return f"""
    <div style="font-family:-apple-system,sans-serif;width:300px;">
      <div style="background:{p['color']};color:white;padding:12px 14px;border-radius:6px 6px 0 0;">
        <div style="font-size:15px;font-weight:700;">{p['name']}</div>
        <div style="font-size:11px;opacity:.85;margin-top:2px;">{p['subtitle']}</div>
      </div>
      <div style="padding:12px 14px;background:white;border:1px solid {p['color']}44;border-radius:0 0 6px 6px;">
        <div style="font-size:11px;color:#888;margin-bottom:6px;">📍 {p['location']} &nbsp;·&nbsp; {p['years']}</div>
        <div style="font-size:12px;color:#333;line-height:1.5;margin-bottom:10px;">{p['brief']}</div>
        <div style="background:{sc}18;border-left:3px solid {sc};padding:8px 10px;border-radius:0 4px 4px 0;font-size:11px;color:#333;">
          <strong style="color:{sc};">{emoji} {p['status']}</strong><br>{preview}
        </div>
      </div>
    </div>"""


def marker_html(color: str, selected: bool) -> str:
    sz = 44 if selected else 34
    border = "4px solid gold" if selected else "3px solid white"
    anchor_y = sz
    return (
        f'<div style="width:{sz}px;height:{sz}px;background:{color};'
        f'border-radius:50% 50% 50% 0;transform:rotate(-45deg);'
        f'border:{border};box-shadow:2px 2px 8px rgba(0,0,0,.45);"></div>'
    ), sz, anchor_y


def build_map(selected_id: str | None = None) -> folium.Map:
    if selected_id:
        proj = next((p for p in PROJECTS if p["id"] == selected_id), None)
        center = proj["coords"] if proj else [52.2, -3.0]
        zoom = 10
    else:
        center = [52.2, -3.0]
        zoom = 7

    m = folium.Map(location=center, zoom_start=zoom, tiles="CartoDB positron", prefer_canvas=True)

    for p in PROJECTS:
        is_sel = p["id"] == selected_id
        html, sz, ay = marker_html(p["color"], is_sel)
        folium.Marker(
            location=p["coords"],
            popup=folium.Popup(popup_html(p), max_width=320),
            tooltip=folium.Tooltip(f"<b>{p['name']}</b><br><small>{p['type']}</small>"),
            icon=folium.DivIcon(html=html, icon_size=(sz, sz), icon_anchor=(sz // 2, ay)),
        ).add_to(m)

    return m


def overview_page():
    st.markdown(
        """
        <div class="project-header" style="background:linear-gradient(135deg,#1a1a2e,#0f3460);">
          <h1 style="margin:0;font-size:2rem;">🏗️ Arup UK Projects</h1>
          <p style="margin:.5rem 0 0;opacity:.85;font-size:1.05rem;">
            Infrastructure across England &amp; Wales worked on during 2 years at Arup · 2016–2018
          </p>
        </div>""",
        unsafe_allow_html=True,
    )

    map_col, list_col = st.columns([3, 2])

    with map_col:
        m = build_map()
        st_folium(m, use_container_width=True, height=520, returned_objects=[])

    with list_col:
        st.markdown("### All Projects")
        for p in PROJECTS:
            emoji = STATUS_EMOJI.get(p["status"], "📍")
            sc = p["status_color"]
            st.markdown(
                f"""<div class="project-card" style="border-left-color:{p['color']};">
                  <div style="font-weight:600;color:#1a1a2e;">{p['name']}</div>
                  <div style="font-size:12px;color:#666;margin:2px 0 6px;">{p['location']}</div>
                  <span style="background:{sc};color:white;padding:2px 10px;border-radius:10px;font-size:11px;">
                    {emoji} {p['status']}
                  </span>
                </div>""",
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.caption(
        "Click a project in the sidebar to explore its history and current status. "
        "Click any map marker to see a summary popup."
    )


def project_page(proj: dict):
    sc = proj["status_color"]
    emoji = STATUS_EMOJI.get(proj["status"], "📍")

    st.markdown(
        f"""<div class="project-header" style="background:linear-gradient(135deg,{proj['color']}cc,{proj['color']}88);">
          <h1 style="margin:0;font-size:1.9rem;">{proj['name']}</h1>
          <p style="margin:.3rem 0 .9rem;opacity:.9;">{proj['subtitle']} &nbsp;·&nbsp; {proj['location']}</p>
          <span style="background:rgba(255,255,255,.25);color:white;padding:3px 12px;border-radius:20px;font-size:.75rem;font-weight:700;">
            {proj['type']}
          </span>&nbsp;
          <span style="background:{sc};color:white;padding:3px 12px;border-radius:20px;font-size:.75rem;font-weight:700;">
            {emoji} {proj['status']}
          </span>&nbsp;
          <span style="background:rgba(255,255,255,.2);color:white;padding:3px 12px;border-radius:20px;font-size:.75rem;">
            📅 {proj['years']}
          </span>
        </div>""",
        unsafe_allow_html=True,
    )

    map_col, detail_col = st.columns([1, 1])

    with map_col:
        m = build_map(proj["id"])
        st_folium(m, use_container_width=True, height=420, returned_objects=[])

    with detail_col:
        st.markdown("#### About the Project")
        for para in proj["description"].split("\n\n"):
            st.markdown(para)

        st.markdown(
            f"""<div class="detail-box" style="border-left-color:{sc};">
              <div style="font-size:.75rem;font-weight:700;color:{sc};text-transform:uppercase;margin-bottom:8px;">
                {emoji} Current Status — {proj['status']}
              </div>
              <div style="font-size:.9rem;color:#333;line-height:1.65;">
                {proj['status_detail']}
              </div>
            </div>""",
            unsafe_allow_html=True,
        )


def main():
    with st.sidebar:
        st.markdown("## 🏗️ Arup Projects")
        st.markdown("*UK Infrastructure · 2016–2018*")
        st.divider()

        options = ["🗺️  All Projects Overview"] + [
            f"{STATUS_EMOJI.get(p['status'], '📍')}  {p['name']}" for p in PROJECTS
        ]
        selected_idx = st.radio("Navigate:", range(len(options)), format_func=lambda i: options[i], index=0)

        st.divider()
        st.markdown(
            "<small>Six infrastructure projects across England and Wales. "
            "Select a project to explore its history and current status.</small>",
            unsafe_allow_html=True,
        )

    if selected_idx == 0:
        overview_page()
    else:
        project_page(PROJECTS[selected_idx - 1])


if __name__ == "__main__":
    main()
