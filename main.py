import flet as ft


def main(page: ft.Page):
    page.title = "Silvanus Inekela Mbango Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#071739"
    page.scroll = "auto"
    page.padding = 20

    # HEADER SECTION
    header = ft.Container(
        content=ft.Column([
            ft.Text(
                "SILVANUS INEKELA MBANGO",
                size=34,
                weight=ft.FontWeight.BOLD,
                color="white",
            ),
            ft.Text(
                "Computer Programming I | Web Portfolio 2026",
                size=18,
                color="#9bbcff",
            ),
            ft.Text(
                "GitHub Manager • Firestore Contributor • Bug Fixing • Team Collaboration",
                size=14,
                color="white70",
            ),
        ]),
        padding=20,
        border_radius=20,
        bgcolor="#0b2447",
    )

    # BIO SECTION
    bio = ft.Container(
        content=ft.Column([
            ft.Text("Professional Bio", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),
            ft.Text(
                "Silvanus Inekela Mbango is a motivated and innovative Computer Programming student with a strong passion for software development, engineering technologies, and modern web systems. Throughout the semester, he actively contributed to the group project by coordinating GitHub repository activities, assisting with Firestore integration, fixing bugs, improving interface responsiveness, and supporting collaboration between team members. His interest in technology and engineering continues to drive his growth in software development and problem-solving.",
                size=15,
                color="white70",
            ),
        ]),
        padding=20,
        border_radius=20,
        bgcolor="#102c57",
    )

    # TIMELINE SECTION
    timeline = ft.Container(
        content=ft.Column([
            ft.Text("Project Timeline", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),

            ft.Text("Week 1 - Repository setup and project planning", color="white70"),
            ft.Text("Week 2 - Assisted with Firestore database configuration", color="white70"),
            ft.Text("Week 3 - Participated in UI improvement discussions", color="white70"),
            ft.Text("Week 4 - Fixed interface bugs and tested features", color="white70"),
            ft.Text("Week 5 - Managed GitHub repository commits and updates", color="white70"),
            ft.Text("Week 6 - Improved project structure and collaborated on debugging", color="white70"),
            ft.Text("Week 7 - Assisted team members with integration issues", color="white70"),
            ft.Text("Week 8 - Final testing and deployment preparation", color="white70"),
        ]),
        padding=20,
        border_radius=20,
        bgcolor="#0b2447",
    )

    # MATLAB SECTION
    matlab = ft.Container(
        content=ft.Column([
            ft.Text("MATLAB Achievement Hub", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),

            ft.Text("✔ MATLAB Onramp", color="white70"),
            ft.Text("✔ calculationss with vectors & matrices", color="white70"),
            ft.Text("✔ solve systems of first order ODEs", color="white70"),
            ft.Text("✔ Machine Learning Onramp", color="white70"),
            ft.Text("✔ MATLAB desktop tools & troubleshootings scripts", color="white70"),
            ft.Text("✔ Explore data with Matlab plots", color="white70"),

            ft.Text(
                "Certificates available in PDF format.",
                t.Text("📄 View Certificates:", size=14, weight=ft.FontWeight.BOLD, color="#9bbcff"),
ft.Text("All 6 MATLAB certificates are stored in the GitHub repository", size=12, color="white70"),
ft.Text("GitHub Link: github.com/silverna-creator/portfolio/tree/main/certificates", size=12, color="#9bbcff"),
                italic=True,
                color="#9bbcff",
            ),
        ]),
        padding=20,
        border_radius=20,
        bgcolor="#102c57",
    )

    # BLOG SECTION
    blog = ft.Container(
        content=ft.Column([
            ft.Text("Confidence in Concepts", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),

            ft.Text(
                "Understanding Firestore Databases",
                size=20,
                weight=ft.FontWeight.BOLD,
                color="#9bbcff",
            ),
            ft.Text(
                "Firestore is a cloud-based NoSQL database provided by Google Firebase. It allows applications to store and sync data in real time. During the project, Firestore was explored for efficient data handling, user information management, and improving synchronization between different components of the system.",
                color="white70",
            ),

            ft.Text(
                "Debugging and Problem Solving",
                size=20,
                weight=ft.FontWeight.BOLD,
                color="#9bbcff",
            ),
            ft.Text(
                "Debugging plays an important role in software development. Various interface and logic issues were identified and corrected during the semester. Fixing bugs improved application stability, user interaction, and overall functionality.",
                color="white70",
            ),

            ft.Text(
                "GitHub Collaboration",
                size=20,
                weight=ft.FontWeight.BOLD,
                color="#9bbcff",
            ),
            ft.Text(
                "GitHub was used for version control and collaboration throughout the project. Repository management included organizing commits, reviewing updates, monitoring changes, and assisting with project coordination among group members.",
                color="white70",
            ),
        ]),
        padding=20,
        border_radius=20,
        bgcolor="#0b2447",
    )

    # GITHUB SECTION
    github = ft.Container(
        content=ft.Column([
            ft.Text("GitHub Evidence", size=26, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(color="white24"),

            ft.Text("• Managed repository commits and updates", color="white70"),
            ft.Text("• Assisted with feature integration and debugging", color="white70"),
            ft.Text("• Participated in collaborative project reviews", color="white70"),
            ft.Text("• Helped organize repository structure and workflow", color="white70"),
            ft.Text("• Contributed to project deployment preparation", color="white70"),

            ft.Text(
                "Impact Summary:",
                size=18,
                weight=ft.FontWeight.BOLD,
                color="#9bbcff",
            ),
            ft.Text(
                "The contributions made throughout the project improved workflow coordination, reduced system errors, and strengthened collaboration among team members. Repository management and debugging support helped maintain project consistency and stability.",
                color="white70",
            ),
        ]),
        padding=20,
        border_radius=20,
        bgcolor="#102c57",
    )

    # FOOTER
    footer = ft.Container(
        content=ft.Text(
            "© 2026 Silvanus Inekela Mbango | Computer Programming I Portfolio",
            color="white54",
            size=12,
        ),
        padding=20,
    )

    # PAGE LAYOUT
    page.add(
        header,
        ft.Container(height=15),
        bio,
        ft.Container(height=15),
        timeline,
        ft.Container(height=15),
        matlab,
        ft.Container(height=15),
        blog,
        ft.Container(height=15),
        github,
        ft.Container(height=20),
        footer,
    )


ft.app(target=main)