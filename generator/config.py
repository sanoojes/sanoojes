SKILLS = [
    {
        "title": "Languages",
        "items": [
            {"name": "JavaScript", "icon": "javascript.svg", "remote": "JavaScript.svg", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript"},
            {"name": "TypeScript", "icon": "typescript.svg", "remote": "TypeScript.svg", "url": "https://www.typescriptlang.org/"},
            {"name": "HTML5", "icon": "html.svg", "remote": "HTML.svg", "url": "https://developer.mozilla.org/en-US/docs/Web/HTML"},
            {"name": "CSS3", "icon": "css.svg", "remote": "CSS.svg", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS"},
            {"name": "C", "icon": "c.svg", "remote": "C.svg", "url": "https://en.cppreference.com/w/c"},
            {"name": "Rust", "icon": "rust.svg", "remote": "Rust.svg", "url": "https://www.rust-lang.org/"},
            {"name": "Python", "icon": "python.svg", "remote": "Python-Dark.svg", "url": "https://www.python.org/"},
            {"name": "Java", "icon": "java.svg", "remote": "Java-Dark.svg", "url": "https://www.java.com/"},
        ],
    },
    {
        "title": "Frameworks & Runtimes",
        "items": [
            {"name": "React", "icon": "react.svg", "remote": "React-Dark.svg", "url": "https://react.dev/"},
            {"name": "Next.js", "icon": "nextjs.svg", "remote": "NextJS-Dark.svg", "url": "https://nextjs.org/"},
            {"name": "Svelte", "icon": "svelte.svg", "remote": "Svelte.svg", "url": "https://svelte.dev/"},
            {"name": "ElysiaJS", "icon": "elysia.svg", "remote": "Elysia-Dark.svg", "url": "https://elysiajs.com/"},
            {"name": "Bun", "icon": "bun.svg", "remote": "Bun-Dark.svg", "url": "https://bun.sh/"},
            {"name": "Node.js", "icon": "nodejs.svg", "remote": "NodeJS-Dark.svg", "url": "https://nodejs.org/"},
        ],
    },
    {
        "title": "Databases",
        "items": [
            {"name": "PostgreSQL", "icon": "postgres.svg", "remote": "PostgreSQL-Dark.svg", "url": "https://www.postgresql.org/"},
            {"name": "Redis", "icon": "redis.svg", "remote": "Redis-Dark.svg", "url": "https://redis.io/"},
            {"name": "MySQL", "icon": "mysql.svg", "remote": "MySQL-Dark.svg", "url": "https://www.mysql.com/"},
        ],
    },
    {
        "title": "Cybersecurity & Infrastructure",
        "items": [
            {"name": "Kali Linux", "icon": "kali.svg", "remote": "Kali-Dark.svg", "url": "https://www.kali.org/"},
            {"name": "Linux", "icon": "linux.svg", "remote": "Linux-Dark.svg", "url": "https://www.kernel.org/"},
            {"name": "Bash", "icon": "bash.svg", "remote": "Bash-Dark.svg", "url": "https://www.gnu.org/software/bash/"},
            {"name": "Docker", "icon": "docker.svg", "remote": "Docker.svg", "url": "https://www.docker.com/"},
            {"name": "Git", "icon": "git.svg", "remote": "Git.svg", "url": "https://git-scm.com/"},
        ],
    },
]

SOCIALS = [
    {"name": "Instagram", "icon": "instagram.svg", "remote": "Instagram.svg", "url": "https://sanooj.uk/instagram"},
    {"name": "Discord", "icon": "discord.svg", "remote": "Discord.svg", "url": "https://sanooj.uk/discord"},
    {"name": "Twitter", "icon": "twitter.svg", "remote": "Twitter.svg", "url": "https://sanooj.uk/twitter"},
    {"name": "Email", "icon": "gmail.svg", "remote": "Gmail-Dark.svg", "url": "mailto:mail@sanooj.es"},
]

# For downloading custom icons
CUSTOM_ICONS = [
    # Add custom icons here with:
    # "source": "local"     - use local file in assets/icons/
    # "source": "url"       - download from custom URL (set "remote" to full URL)
    # "source": "skillicons" - default, download from skillicons repo (default)
]

CERTIFICATIONS = [
    {
        "name": "Certified Ethical Hacker (CEH v13)",
        "issuer": "EC-Council",
        "badge": "./assets/CEH_badge.png",
        "badge_height": 96,
        "badge_alt": "CEH v13 Badge",
        "certificate_url": "https://documents.sanooj.uk/CEH.pdf",
        "verify_url": "https://aspen.eccouncil.org/Verify",
        "cert_badge_url": "https://img.shields.io/badge/View-Certificate-E11D48?style=flat-square&logoColor=white",
        "verify_badge_url": "https://img.shields.io/badge/Aspen-Verify%20Credential-10B981?style=flat-square&logo=checkmarx&logoColor=white",
    }
]

ACHIEVEMENTS = [
    {
        "name": "NASA Space Apps Challenge 2025 - 3rd Place",
        "issuer": "Amal Jyothi College of Engineering Autonomous",
        "date": "Oct 2025",
        "image": "./assets/thumbnails/nasa-space-apps-3rd-place.jpg",
        "image_height": 64,
        "certificate_url": "https://documents.sanooj.uk/nasa-space-apps-3rd-place.pdf",
        "verify_url": "https://events.amaljyothi.ac.in/verify/qzh6qk",
    },
    {
        "name": "HOGWARTS ETERNAL CTF - 1st Runner Up",
        "issuer": "Offenso Academy",
        "date": "2025",
        "image": "./assets/thumbnails/Hogwarts-Eternal-CTF.jpg",
        "image_height": 64,
        "certificate_url": "https://documents.sanooj.uk/Hogwarts-Eternal-CTF.pdf",
        "verify_url": "",
    },
]

TEMPLATE_VARS = {
    "NAME": "Sanooj Es",
    "BIO": "I'm a full-stack developer and ethical hacker (CEH). I write code in Typescript, Python, Rust and C, and I do penetration testing and random projects.",
    "GITHUB_USERNAME": "sanoojes",
    "WAKATIME_USERNAME": "23888",
    "DISCORD_ID": "821653196161679371",
    "KOFI_URL": "https://ko-fi.com/sanoojes",
}