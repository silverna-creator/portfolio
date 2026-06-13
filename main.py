import flet as ft

# Raw GitHub URLs (use after you push images)
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

    # Header with profile picture (local path, works after you place profile.jpeg in certificates folder)
    profile_img = ft.Image(src="certificates/profile.jpeg", width=120, height=120, fit="contain", border_radius=60)
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
            ft.Text("Silvanus Inekela Mbango is a motivated and innovative Computer Programming student with a strong passion for software development, engineering technologies, and modern web systems. Throughout the semester, he actively contributed to the group project by coordinating GitHub repository activities, assisting with Firestore integration, fixing bugs, improving interface responsiveness, and supporting collaboration between team members.", size=16, color="white70"),
        ]),
        padding=20, bgcolor="#102c57", border_radius=20,
    )

    timeline = ft.Container(
        content=ft.Column([
            ft.Text("Project Timeline", size=28, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("• Week 1 - Repository setup and project planning", color="white70", size=15),
            ft.Text("• Week 2 - Assisted with Firestore database configuration", color="white70", size=15),
            ft.Text("• Week 3 - Participated in UI improvement discussions", color="white70", size=15),
            ft.Text("• Week 4 - Fixed interface bugs and tested features", color="white70", size=15),
            ft.Text("• Week 5 - Managed GitHub repository commits and updates", color="white70", size=15),
            ft.Text("• Week 6 - Improved project structure and collaborated on debugging", color="white70", size=15),
            ft.Text("• Week 7 - Assisted team members with integration issues", color="white70", size=15),
            ft.Text("• Week 8 - Final testing and deployment preparation", color="white70", size=15),
        ]),
        padding=20, bgcolor="#0b2447", border_radius=20,
    )

    # MATLAB certificates – each has a large image + a visible link below it
    cert_cards = []
    for cert in CERTIFICATES:
        cert_cards.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(cert["name"], size=18, weight=ft.FontWeight.BOLD, color="#9bbcff", text_align="center"),
                    ft.Image(src=cert["img"], width=450, height=None, fit="contain", border_radius=10),
                    ft.TextButton("🔍 Click to view full certificate", url=cert["img"], style=ft.ButtonStyle(color="#9bbcff")),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                padding=15, bgcolor="#1a3a5f", border_radius=15,
            )
        )

    matlab = ft.Container(
        content=ft.Column([
            ft.Text("MATLAB Achievement Hub", size=32, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("✅ 7 Certificates Completed (MathWorks Learning Center)", size=18, color="#9bbcff"),
            ft.GridView(controls=cert_cards, runs_count=2, spacing=20, run_spacing=20, max_extent=550),
            ft.Text("📂 All certificates are also stored in the GitHub repository", size=14, color="white70"),
        ]),
        padding=20, bgcolor="#102c57", border_radius=20,
    )

    # Blog with math notation
    blog = ft.Container(
        content=ft.Column([
            ft.Text("Confidence in Concepts", size=32, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("📐 Mathematical Notation Example:", size=20, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ft.Text("Total Cost = Σ(Qᵢ × Pᵢ) + Overheads", italic=True, size=18, color="white70"),
            ft.Divider(height=20, color="transparent"),
            ft.Text("Understanding Firestore Databases", size=22, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ft.Text("Firestore is a cloud-based NoSQL database provided by Google Firebase. It allows applications to store and sync data in real time. During the project, Firestore was explored for efficient data handling, user information management, and improving synchronization between different components of the system.", size=16, color="white70"),
            ft.Text("Debugging and Problem Solving", size=22, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ft.Text("Debugging plays an important role in software development. Various interface and logic issues were identified and corrected during the semester. Fixing bugs improved application stability, user interaction, and overall functionality.", size=16, color="white70"),
            ft.Text("GitHub Collaboration", size=22, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ft.Text("GitHub was used for version control and collaboration throughout the project. Repository management included organizing commits, reviewing updates, monitoring changes, and assisting with project coordination among group members.", size=16, color="white70"),
        ]),
        padding=20, bgcolor="#0b2447", border_radius=20,
    )

    # GitHub evidence – large images + clickable links below
    evidence_cards = []
    for ev in GITHUB_EVIDENCE:
        evidence_cards.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(ev["title"], size=20, weight=ft.FontWeight.BOLD, color="#9bbcff", text_align="center"),
                    ft.Image(src=ev["img"], width=500, height=None, fit="contain", border_radius=10),
                    ft.TextButton("🔍 Click to view full image", url=ev["img"], style=ft.ButtonStyle(color="#9bbcff")),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                padding=15, bgcolor="#1a3a5f", border_radius=15,
            )
        )

    github = ft.Container(
        content=ft.Column([
            ft.Text("GitHub Evidence", size=32, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text("📸 Screenshots of my contributions (click the link below each image to enlarge):", size=18, color="white70"),
            ft.ResponsiveRow(evidence_cards, spacing=20, run_spacing=20),
            ft.Divider(height=15, color="transparent"),
            ft.Text("• Managed repository commits and updates", size=16, color="white70"),
            ft.Text("• Assisted with feature integration and debugging", size=16, color="white70"),
            ft.Text("• Participated in collaborative project reviews", size=16, color="white70"),
            ft.Text("Impact Summary:", size=20, weight=ft.FontWeight.BOLD, color="#9bbcff"),
            ft.Text("The contributions made throughout the project improved workflow coordination, reduced system errors, and strengthened collaboration among team members. Repository management and debugging support helped maintain project consistency and stability.", size=16, color="white70"),
        ]),
        padding=20, bgcolor="#102c57", border_radius=20,
    )

    footer = ft.Container(
        content=ft.Text("© 2026 Silvanus Inekela Mbango | Computer Programming I Portfolio", size=14, color="white54", text_align="center"),
        padding=20,
    )

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