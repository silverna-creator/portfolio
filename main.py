import flet as ft
import flet_video as ftv

# Raw GitHub URLs (works locally and on Render)
BASE_URL = "https://raw.githubusercontent.com/silverna-creator/portfolio/main"

CERTIFICATES = [
    {"name": "MATLAB Onramp", "img": f"{BASE_URL}/certificates/matab_onramp.jpeg"},
    {"name": "Vectors & Matrices", "img": f"{BASE_URL}/certificates/vectors_matrices.jpeg"},
    {"name": "Solve First Order ODEs", "img": f"{BASE_URL}/certificates/odes.jpeg"},
    {"name": "Machine Learning Onramp", "img": f"{BASE_URL}/certificates/ml_onramp.jpeg"},
    {"name": "MATLAB Desktop Tools", "img": f"{BASE_URL}/certificates/desktop_tools.jpeg"},
    {"name": "Troubleshooting Scripts", "img": f"{BASE_URL}/certificates/troubleshooting.jpeg"},
    {"name": "Explore Data with Plots", "img": f"{BASE_URL}/certificates/data_plots.jpeg"},
]

GITHUB_EVIDENCE = [
    {"title": "Commit History", "img": f"{BASE_URL}/github%20evidence/commits_history.jpeg"},
    {"title": "Pull Request Logs", "img": f"{BASE_URL}/github%20evidence/pull_requests.jpeg"},
]

def main(page: ft.Page):
    page.title = "Silvanus Inekela Mbango Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#071739"
    page.scroll = "auto"
    page.padding = 20

    # Profile picture (raw GitHub URL, larger size)
    profile_img = ft.Image(src="certificates/profile.jpeg", width=160, height=160, fit="contain", border_radius=80)

    header = ft.Container(
        content=ft.Column([
            ft.Row([profile_img], alignment=ft.MainAxisAlignment.CENTER),
            ft.Text("SILVANUS INEKELA MBANGO", size=34, weight=ft.FontWeight.BOLD, color="white", text_align="center"),
            ft.Text("Computer Programming I | Web Portfolio 2026", size=18, color="#9bbcff", text_align="center"),
            ft.Text("GitHub Manager • Firestore Contributor • Bug Fixing • Team Collaboration", size=14, color="white70", text_align="center"),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=20, bgcolor="#0b2447", border_radius=20,
    )

    bio = ft.Container(
        content=ft.Column([
            ft.Text("Professional Bio", size=28, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("Silvanus Inekela Mbango is a motivated and innovative Computer Programming student...", size=16, color="white70"),
        ]),
        padding=20, bgcolor="#102c57", border_radius=20,
    )

    timeline = ft.Container(
        content=ft.Column([
            ft.Text("Project Timeline", size=28, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("• Week 1 - Repository setup", color="white70", size=15),
            ft.Text("• Week 2 - Firestore configuration", color="white70", size=15),
            ft.Text("• Week 3 - UI improvements", color="white70", size=15),
            ft.Text("• Week 4 - Bug fixing", color="white70", size=15),
            ft.Text("• Week 5 - GitHub commits", color="white70", size=15),
            ft.Text("• Week 6 - Debugging", color="white70", size=15),
            ft.Text("• Week 7 - Integration", color="white70", size=15),
            ft.Text("• Week 8 - Deployment", color="white70", size=15),
        ]),
        padding=20, bgcolor="#0b2447", border_radius=20,
    )

    # MATLAB certificates
    cert_cards = []
    for cert in CERTIFICATES:
        cert_cards.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(cert["name"], size=18, weight=ft.FontWeight.BOLD, color="#9bbcff", text_align="center"),
                    ft.Image(src=cert["img"], width=450, height=None, fit="contain", border_radius=10),
                    ft.TextButton("🔍 View full certificate", url=cert["img"], style=ft.ButtonStyle(color="#9bbcff")),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                padding=15, bgcolor="#1a3a5f", border_radius=15,
            )
        )

    matlab = ft.Container(
        content=ft.Column([
            ft.Text("MATLAB Achievement Hub", size=32, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("✅ 7 Certificates Completed", size=18, color="#9bbcff"),
            ft.GridView(controls=cert_cards, runs_count=2, spacing=20, run_spacing=20, max_extent=550),
        ]),
        padding=20, bgcolor="#102c57", border_radius=20,
    )

    # Blog with embedded video (replace VIDEO_URL with your direct .mp4 link)
    VIDEO_URL = "https://files.catbox.moe/pf6r3e.mp4" # <-- CHANGE THIS to your direct video URL

    blog = ft.Container(
        content=ft.Column([
            ft.Text("Confidence in Concepts", size=32, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("📐 Mathematical Notation Example:", size=20, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ft.Text("Total Cost = Σ(Qᵢ × Pᵢ) + Overheads", italic=True, size=18, color="white70"),
            ft.Divider(height=20, color="transparent"),
            ft.Text("🎥 Project Explanation (1 min 20 sec):", size=20, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ftv.Video(
                playlist=[ftv.VideoMedia(VIDEO_URL)],
                autoplay=False,
                volume=100,
                aspect_ratio=16/9,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Text("Understanding Firestore Databases", size=22, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ft.Text("Firestore is a cloud-based NoSQL database...", size=16, color="white70"),
            ft.Text("Debugging and Problem Solving", size=22, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ft.Text("Debugging plays an important role...", size=16, color="white70"),
            ft.Text("GitHub Collaboration", size=22, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ft.Text("GitHub was used for version control...", size=16, color="white70"),
        ]),
        padding=20, bgcolor="#0b2447", border_radius=20,
    )

    # GitHub evidence
    evidence_cards = []
    for ev in GITHUB_EVIDENCE:
        evidence_cards.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(ev["title"], size=20, weight=ft.FontWeight.BOLD, color="#9bbcff", text_align="center"),
                    ft.Image(src=ev["img"], width=500, height=None, fit="contain", border_radius=10),
                    ft.TextButton("🔍 View full image", url=ev["img"], style=ft.ButtonStyle(color="#9bbcff")),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                padding=15, bgcolor="#1a3a5f", border_radius=15,
            )
        )

    github = ft.Container(
        content=ft.Column([
            ft.Text("GitHub Evidence", size=32, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.ResponsiveRow(evidence_cards, spacing=20, run_spacing=20),
            ft.Text("• Managed repository commits", size=16, color="white70"),
            ft.Text("Impact Summary: Improved workflow coordination", size=16, color="white70"),
        ]),
        padding=20, bgcolor="#102c57", border_radius=20,
    )

    footer = ft.Container(
        content=ft.Text("© 2026 Silvanus Inekela Mbango", size=14, color="white54", text_align="center"),
        padding=20,
    )

    page.add(header, bio, timeline, matlab, blog, github, footer)

ft.app(target=main)