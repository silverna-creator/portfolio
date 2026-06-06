import flet as ft

# Raw GitHub URLs (always work on Render)
CERTIFICATES = [
    {"name": "MATLAB Onramp", "img": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/matab_onramp.jpeg"},
    {"name": "Vectors & Matrices", "img": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/vectors_matrices.jpeg"},
    {"name": "Solve First Order ODEs", "img": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/odes.jpeg"},
    {"name": "Machine Learning Onramp", "img": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/ml_onramp.jpeg"},
    {"name": "MATLAB Desktop Tools", "img": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/desktop_tools.jpeg"},
    {"name": "Troubleshooting Scripts", "img": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/troubleshooting.jpeg"},
    {"name": "Explore Data with Plots", "img": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/data_plots.jpeg"},
]

GITHUB_EVIDENCE = [
    {"title": "Commit History", "img": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/github%20evidence/commits_history.jpeg"},
    {"title": "Pull Request Logs", "img": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/github%20evidence/pull_requests.jpeg"},
]

def main(page: ft.Page):
    page.title = "Silvanus Inekela Mbango Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#071739"
    page.scroll = "auto"
    page.padding = 20

    header = ft.Container(
        content=ft.Column([
            ft.Text("SILVANUS INEKELA MBANGO", size=34, weight=ft.FontWeight.BOLD, color="white"),
            ft.Text("Computer Programming I | Web Portfolio 2026", size=18, color="#9bbcff"),
            ft.Text("GitHub Manager • Firestore Contributor • Bug Fixing • Team Collaboration", size=14, color="white70"),
        ]),
        padding=20, bgcolor="#0b2447", border_radius=20,
    )

    bio = ft.Container(
        content=ft.Column([
            ft.Text("Professional Bio", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("Silvanus Inekela Mbango is a motivated and innovative Computer Programming student...", size=15, color="white70"),
        ]),
        padding=20, bgcolor="#102c57", border_radius=20,
    )

    timeline = ft.Container(
        content=ft.Column([
            ft.Text("Project Timeline", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("Week 1 - Repository setup", color="white70"),
            ft.Text("Week 2 - Firestore configuration", color="white70"),
            ft.Text("Week 3 - UI improvements", color="white70"),
            ft.Text("Week 4 - Bug fixing", color="white70"),
            ft.Text("Week 5 - GitHub commits", color="white70"),
            ft.Text("Week 6 - Debugging", color="white70"),
            ft.Text("Week 7 - Integration", color="white70"),
            ft.Text("Week 8 - Deployment", color="white70"),
        ]),
        padding=20, bgcolor="#0b2447", border_radius=20,
    )

    # Certificate images
    cert_cards = []
    for cert in CERTIFICATES:
        cert_cards.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(cert["name"], size=16, weight=ft.FontWeight.BOLD, color="#9bbcff"),
                    ft.Image(src=cert["img"], width=400, height=None, fit="contain", border_radius=10),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                padding=10, bgcolor="#1a3a5f", border_radius=12,
            )
        )

    matlab = ft.Container(
        content=ft.Column([
            ft.Text("MATLAB Achievement Hub", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("✅ 7 Certificates Completed (MathWorks Learning Center)", size=14, color="#9bbcff"),
            ft.GridView(controls=cert_cards, runs_count=2, spacing=10, run_spacing=10, max_extent=450),
            ft.Text("📂 All certificates are stored in the GitHub repository", size=12, color="white70"),
        ]),
        padding=20, bgcolor="#102c57", border_radius=20,
    )

    blog = ft.Container(
        content=ft.Column([
            ft.Text("Confidence in Concepts", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("Understanding Firestore", size=20, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ft.Text("Firestore is a cloud NoSQL database...", color="white70"),
            ft.Text("Debugging & Problem Solving", size=20, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ft.Text("Debugging improves stability...", color="white70"),
            ft.Text("GitHub Collaboration", size=20, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ft.Text("GitHub for version control...", color="white70"),
        ]),
        padding=20, bgcolor="#0b2447", border_radius=20,
    )

    # GitHub evidence images
    evidence_cards = []
    for ev in GITHUB_EVIDENCE:
        evidence_cards.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(ev["title"], size=16, weight=ft.FontWeight.BOLD, color="#9bbcff"),
                    ft.Image(src=ev["img"], width=400, height=None, fit="contain", border_radius=10),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                padding=10, bgcolor="#1a3a5f", border_radius=12,
            )
        )

    github = ft.Container(
        content=ft.Column([
            ft.Text("GitHub Evidence", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("📸 Screenshots of my contributions:", size=16, color="white70"),
            ft.ResponsiveRow(evidence_cards, spacing=20, run_spacing=20),
            ft.Text("• Managed repository commits and updates", color="white70"),
            ft.Text("• Assisted with feature integration and debugging", color="white70"),
            ft.Text("• Participated in collaborative project reviews", color="white70"),
            ft.Text("Impact Summary: Improved workflow coordination", color="white70"),
        ]),
        padding=20, bgcolor="#102c57", border_radius=20,
    )

    footer = ft.Container(content=ft.Text("© 2026 Silvanus Inekela Mbango", color="white54", size=12), padding=20)

    page.add(
        header, ft.Container(height=15),
        bio, ft.Container(height=15),
        timeline, ft.Container(height=15),
        matlab, ft.Container(height=15),
        blog, ft.Container(height=15),
        github, ft.Container(height=20),
        footer,
    )

ft.app(target=main)
