#!/usr/bin/env python3
from html import escape
from pathlib import Path
from config import SKILLS, SOCIALS, CERTIFICATIONS, ACHIEVEMENTS, TEMPLATE_VARS, DEFAULT_CERT_BADGE, DEFAULT_VERIFY_BADGE

CURRENT_DIR = Path(__file__).resolve().parent
ROOT_DIR = CURRENT_DIR.parent
TEMPLATE_PATH = CURRENT_DIR / "template.md"
OUTPUT_PATH = ROOT_DIR / "README.md"



def render_icons(items, height=36, separator="\n", indent=""):
    lines = [
        f'{indent}<a href="{item["url"]}" target="_blank" rel="noopener noreferrer">'
        f'<img src="./assets/icons/{item["icon"]}" height="{height}" alt="{escape(item["name"])}" /></a>'
        for item in items
    ]
    return separator.join(lines)


def build_action_badges(item, separator="<br />\n        "):
    badges = []

    cert_url = item.get("certificate_url")
    if cert_url:
        cert_badge_url = item.get("cert_badge_url") or DEFAULT_CERT_BADGE
        cert_badge_alt = escape(item.get("cert_badge_alt", "View Certificate"))
        badges.append(
            f'<a href="{cert_url}" target="_blank" rel="noopener noreferrer">'
            f'<img src="{cert_badge_url}" height="20" alt="{cert_badge_alt}" /></a>'
        )

    verify_url = item.get("verify_url")
    if verify_url:
        verify_badge_url = item.get("verify_badge_url") or DEFAULT_VERIFY_BADGE
        verify_badge_alt = escape(item.get("verify_badge_alt", "Verify Credential"))
        badges.append(
            f'<a href="{verify_url}" target="_blank" rel="noopener noreferrer">'
            f'<img src="{verify_badge_url}" height="20" alt="{verify_badge_alt}" /></a>'
        )

    return separator.join(badges)


def build_credential_row(item, is_cert=True):
    name = escape(item.get("name", ""))
    primary_link = item.get("certificate_url") or item.get("verify_url") or "#"
    action_html = build_action_badges(item) or "—"

    if is_cert:
        img_src = item.get("badge", "")
        img_alt = escape(item.get("badge_alt", name or "Certificate"))
        img_tag = f'<img src="{img_src}" height="56" alt="{img_alt}" />'
    else:
        img_src = item.get("image", "")
        img_alt = escape(item.get("image_alt", name or "Achievement"))
        img_tag = f'<img src="{img_src}" width="96" alt="{img_alt}" />'

    meta_parts = [escape(p) for p in (item.get("issuer"), item.get("date")) if p]
    meta_html = f'\n        <br /><sub>{" · ".join(meta_parts)}</sub>' if meta_parts else ""

    return (
        "    <tr>\n"
        '      <td width="120" align="center" valign="middle">\n'
        f'        <a href="{primary_link}" target="_blank" rel="noopener noreferrer">\n'
        f"          {img_tag}\n"
        "        </a>\n"
        "      </td>\n"
        '      <td width="580" valign="middle">\n'
        f"        <b>{name}</b>{meta_html}\n"
        "      </td>\n"
        '      <td width="200" align="center" valign="middle">\n'
        f"        {action_html}\n"
        "      </td>\n"
        "    </tr>"
    )


def build_credentials_html():
    rows = []
    for cert in CERTIFICATIONS:
        rows.append(build_credential_row(cert, is_cert=True))
    for ach in ACHIEVEMENTS:
        rows.append(build_credential_row(ach, is_cert=False))

    if not rows:
        return ""

    return (
        "<h2>Credentials &amp; Honors</h2>\n\n"
        "<table>\n"
        "  <thead>\n"
        "    <tr>\n"
        '      <th width="120" align="center">Badge</th>\n'
        '      <th width="580" align="left">Credential</th>\n'
        '      <th width="200" align="center">Verification</th>\n'
        "    </tr>\n"
        "  </thead>\n"
        "  <tbody>\n"
        + "\n".join(rows)
        + "\n  </tbody>\n"
        "</table>"
    )


def build_skills_html():
    if not SKILLS:
        return ""

    thead_rows = []
    tbody_rows = []

    for i in range(0, len(SKILLS), 2):
        pair = SKILLS[i : i + 2]

        if len(pair) == 2:
            left, right = pair
            header_row = (
                "    <tr>\n"
                f'      <th width="450" align="left">{escape(left["title"])}</th>\n'
                f'      <th width="450" align="left">{escape(right["title"])}</th>\n'
                "    </tr>"
            )
            content_row = (
                "    <tr>\n"
                '      <td width="450" valign="middle">\n'
                f'{render_icons(left["items"], height=36, indent="        ")}\n'
                "      </td>\n"
                '      <td width="450" valign="middle">\n'
                f'{render_icons(right["items"], height=36, indent="        ")}\n'
                "      </td>\n"
                "    </tr>"
            )
        else:
            single = pair[0]
            header_row = (
                "    <tr>\n"
                f'      <th colspan="2" width="900" align="left">{escape(single["title"])}</th>\n'
                "    </tr>"
            )
            content_row = (
                "    <tr>\n"
                '      <td colspan="2" width="900" valign="middle">\n'
                f'{render_icons(single["items"], height=36, indent="        ")}\n'
                "      </td>\n"
                "    </tr>"
            )

        if i == 0:
            thead_rows.append(header_row)
        else:
            tbody_rows.append(header_row)
        tbody_rows.append(content_row)

    return (
        "<h2>Tech Stack &amp; Tooling</h2>\n\n"
        "<table>\n"
        "  <thead>\n"
        + "\n".join(thead_rows)
        + "\n  </thead>\n"
        "  <tbody>\n"
        + "\n".join(tbody_rows)
        + "\n  </tbody>\n"
        "</table>"
    )


def build_connect_html():
    if not SOCIALS:
        return ""

    icons_html = render_icons(SOCIALS, height=34, separator="&nbsp;&nbsp;\n  ", indent="")
    return f"<h2>Connect</h2>\n\n<p>\n  {icons_html}\n</p>"


def apply_template_vars(content, vars_dict):
    for key, value in vars_dict.items():
        content = content.replace(f"{{{{{key}}}}}", str(value))
    return content


def main():
    if not TEMPLATE_PATH.exists():
        raise FileNotFoundError(f"Template not found at: {TEMPLATE_PATH}")

    template_content = TEMPLATE_PATH.read_text(encoding="utf-8")

    replacements = {
        "<!-- CREDENTIALS -->": build_credentials_html(),
        "<!-- SKILLS -->": build_skills_html(),
        "<!-- CONNECT -->": build_connect_html(),
    }

    final_content = template_content
    for placeholder, html_block in replacements.items():
        final_content = final_content.replace(placeholder, html_block)

    final_content = apply_template_vars(final_content, TEMPLATE_VARS)

    OUTPUT_PATH.write_text(final_content, encoding="utf-8")
    print("README.md generated successfully")


if __name__ == "__main__":
    main()