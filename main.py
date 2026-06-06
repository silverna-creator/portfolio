import flet as ft

# Raw GitHub URLs to your images (already confirmed working)
CERTIFICATES = [
    {"name": "MATLAB Onramp", "url": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/matab_onramp.jpeg"},
    {"name": "Vectors & Matrices", "url": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/vectors_matrices.jpeg"},
    {"name": "Solve First Order ODEs", "url": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/odes.jpeg"},
    {"name": "Machine Learning Onramp", "url": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/ml_onramp.jpeg"},
    {"name": "MATLAB Desktop Tools", "url": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/desktop_tools.jpeg"},
    {"name": "Troubleshooting Scripts", "url": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/troubleshooting.jpeg"},
    {"name": "Explore Data with Plots", "url": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/certificates/data_plots.jpeg"},
]

GITHUB_EVIDENCE = [
    {"title": "Commit History", "url": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/github%20evidence/commits_history.jpeg"},
    {"title": "Pull Request Logs", "url": "https://raw.githubusercontent.com/silverna-creator/portfolio/main/github%20evidence/pull_requests.jpeg"},
]

def main(page: ft.Page):
    page.title = "Silvanus Inekela Mbango Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#071739"
    page.scroll = "auto"
    page.padding = 20

    # Header
    header = ft.Container(
        content=ft.Column([
            ft.Text("SILVANUS INEKELA MBANGO", size=34, weight=ft.FontWeight.BOLD, color="white"),
            ft.Text("Computer Programming I | Web Portfolio 2026", size=18, color="#9bbcff"),
            ft.Text("GitHub Manager • Firestore Contributor • Bug Fixing • Team Collaboration", size=14, color="white70"),
        ]),
        padding=20, bgcolor="#0b2447", border_radius=20,
    )

    # Bio
    bio = ft.Container(
        content=ft.Column([
            ft.Text("Professional Bio", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("Silvanus Inekela Mbango is a motivated and innovative Computer Programming student...", size=15, color="white70"),
        ]),
        padding=20, bgcolor="#102c57", border_radius=20,
    )

    # Timeline
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

    # MATLAB Certificates as clickable links
    cert_links = []
    for cert in CERTIFICATES:
        cert_links.append(
            ft.Container(
                content=ft.TextButton(cert["name"], url=cert["url"]),
                margin=5,
            )
        )

    matlab = ft.Container(
        content=ft.Column([
            ft.Text("MATLAB Achievement Hub", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("✅ 7 Certificates Completed (MathWorks Learning Center)", size=14, color="#9bbcff"),
            ft.Column(cert_links, spacing=8),
            ft.Text("📂 Click any certificate to view the image", size=12, color="white70"),
        ]),
        padding=20, bgcolor="#102c57", border_radius=20,
    )

    # Blog (shortened)
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

    # GitHub Evidence as clickable links
    evidence_links = []
    for ev in GITHUB_EVIDENCE:
        evidence_links.append(
            ft.Container(
                content=ft.TextButton(ev["title"], url=ev["url"]),
                margin=5,
            )
        )

    github = ft.Container(
        content=ft.Column([
            ft.Text("GitHub Evidence", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("📸 Screenshots of my contributions (click to open):", size=16, color="white70"),
            ft.Column(evidence_links, spacing=8),
            ft.Text("• Managed repository commits and updates", color="white70"),
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
