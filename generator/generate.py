#!/usr/bin/env python3
from pathlib import Path
from config import SKILLS, SOCIALS, CERTIFICATIONS, ACHIEVEMENTS, TEMPLATE_VARS

CURRENT_DIR = Path(__file__).resolve().parent
ROOT_DIR = CURRENT_DIR.parent
TEMPLATE_PATH = CURRENT_DIR / "template.md"
OUTPUT_PATH = ROOT_DIR / "README.md"


def render_icons(items, height=42):
    lines = [
        f'<a href="{item["url"]}" target="_blank" rel="noopener noreferrer">'
        f'<img src="./assets/icons/{item["icon"]}" height="{height}" alt="{item["name"]}" /></a>'
        for item in items
    ]
    return "\n".join(lines)


def build_action_badges(item):
    badges = []

    cert_url = item.get("certificate_url")
    cert_badge_url = item.get("cert_badge_url")
    if cert_url and cert_badge_url:
        cert_badge_alt = item.get("cert_badge_alt", "View Certificate")
        badges.append(
            f'<a href="{cert_url}" target="_blank" rel="noopener noreferrer">'
            f'<img src="{cert_badge_url}" height="20" alt="{cert_badge_alt}" /></a>'
        )

    verify_url = item.get("verify_url")
    verify_badge_url = item.get("verify_badge_url")
    if verify_url:
        if not verify_badge_url:
            verify_badge_url = (
                "https://img.shields.io/badge/Verify%20Credential-10B981"
                "?style=flat-square&logo=checkmarx&logoColor=white"
            )
        verify_badge_alt = item.get("verify_badge_alt", "Verify Credential")
        badges.append(
            f'<a href="{verify_url}" target="_blank" rel="noopener noreferrer">'
            f'<img src="{verify_badge_url}" height="20" alt="{verify_badge_alt}" /></a>'
        )

    return " &nbsp; ".join(badges)


def build_certifications_html():
    if not CERTIFICATIONS:
        return ""

    cards = []
    for cert in CERTIFICATIONS:
        badge_height = cert.get("badge_height", 75)
        badge_alt = cert.get("badge_alt", cert.get("name", "Certificate"))
        badge_src = cert.get("badge", "")
        badge_td_style = cert.get(
            "badge_style",
            "padding: 0 12px 12px 12px; border-left: 1px solid #303030;"
        )

        primary_link = cert.get("verify_url") or cert.get("certificate_url") or "#"
        action_html = build_action_badges(cert)

        badge_img_tag = (
            f'<a href="{primary_link}" target="_blank" rel="noopener noreferrer">'
            f'<img src="{badge_src}" height="{badge_height}" alt="{badge_alt}" />'
            f'</a>'
        )

        parts = [
            f'<b>{cert.get("name", "")}</b>'
        ]
        if cert.get("issuer"):
            parts.append(f'<p>{cert["issuer"]}</p>')
        if action_html:
            parts.append(f'{action_html}')

        name_issuer_html = "<br />\n".join(parts)

        card_table = (
            '<table width="100%" style="max-width: 580px; border-collapse: separate; border-spacing: 0; '
            'border: 1px solid #303030; border-radius: 14px; overflow: hidden; margin-bottom: 16px;">\n'
            '<tr>\n'
            f'<td valign="middle" style="padding: 12px 16px;">\n{name_issuer_html}\n</td>\n'
            f'<td width="{badge_height + 20}" align="center" valign="middle" style="{badge_td_style}">\n{badge_img_tag}\n</td>\n'
            '</tr>\n'
            '</table>'
        )
        cards.append(card_table)

    return "<h2>Certifications</h2>\n\n" + "\n\n".join(cards)


def build_achievements_html():
    if not ACHIEVEMENTS:
        return ""

    cards = []
    for ach in ACHIEVEMENTS:
        image_height = ach.get("image_height", 60)
        image_width = ach.get("image_width", int(image_height * 16 / 9))
        image_src = ach.get("image", "")
        image_alt = ach.get("image_alt", ach.get("name", "Achievement"))
        image_radius = ach.get("image_radius", 8)

        badge_td_style = ach.get(
            "image_style",
            "padding: 0 12px 12px 12px; border-left: 1px solid #303030;"
        )

        primary_link = ach.get("verify_url") or ach.get("certificate_url") or "#"
        action_html = build_action_badges(ach)

        image_tag = (
            f'<a href="{primary_link}" target="_blank" rel="noopener noreferrer">'
            f'<img src="{image_src}" height="{image_height}" width="{image_width}" '
            f'style="border-radius: {image_radius}px;" alt="{image_alt}" />'
            f'</a>'
        )

        parts = [
            f'<b>{ach.get("name", "")}</b>'
        ]
        if ach.get("issuer"):
            parts.append(f'<sub>{ach["issuer"]}</sub>')
        if ach.get("date"):
            parts.append(f'<sub>{ach["date"]}</sub>')
        if action_html:
            parts.append(f'<br />{action_html}')

        name_issuer_html = "<br />\n".join(parts)

        card_table = (
            '<table width="100%" style="max-width: 580px; border-collapse: separate; border-spacing: 0; '
            'border: 1px solid #303030; border-radius: 14px; overflow: hidden; margin-bottom: 16px;">\n'
            '<tr>\n'
            f'<td valign="middle" style="padding: 12px 16px;">\n{name_issuer_html}\n</td>\n'
            f'<td width="{image_width + 20}" align="center" valign="middle" style="{badge_td_style}">\n{image_tag}\n</td>\n'
            '</tr>\n'
            '</table>'
        )
        cards.append(card_table)

    return "<h2>Achievements</h2>\n\n" + "\n\n".join(cards)


def build_skills_html():
    sections = ['<h2>Skills & Expertise</h2>']
    for cat in SKILLS:
        sections.append(f'<p><strong>{cat["title"]}</strong></p>')
        sections.append(f'<p>\n{render_icons(cat["items"], 42)}\n</p>')
    return "\n".join(sections)


def build_connect_html():
    return (
        '<h2>Connect with Me</h2>\n\n'
        f'<p>\n{render_icons(SOCIALS, 32)}\n</p>'
    )


def apply_template_vars(content, vars_dict):
    for key, value in vars_dict.items():
        content = content.replace(f"{{{{{key}}}}}", str(value))
    return content


def main():
    if not TEMPLATE_PATH.exists():
        raise FileNotFoundError(f"Template not found at: {TEMPLATE_PATH}")

    template_content = TEMPLATE_PATH.read_text(encoding="utf-8")

    certifications_html = build_certifications_html()
    achievements_html = build_achievements_html()
    skills_html = build_skills_html()
    connect_html = build_connect_html()

    final_content = template_content.replace("<!-- CERTIFICATIONS -->", certifications_html)
    final_content = final_content.replace("<!-- ACHIEVEMENTS -->", achievements_html)
    final_content = final_content.replace("<!-- SKILLS -->", skills_html)
    final_content = final_content.replace("<!-- CONNECT -->", connect_html)
    final_content = apply_template_vars(final_content, TEMPLATE_VARS)

    OUTPUT_PATH.write_text(final_content, encoding="utf-8")
    print("README.md generated successfully")


if __name__ == "__main__":
    main()