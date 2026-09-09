# Privacy Policy

**Effective date:** September 8, 2026

This policy explains what data the TypeRacer Stats Discord bot (application ID
`1213306973374644256`) collects, why it collects it, and how to have it removed. The bot is
operated by Keegan Tournay as a personal, non-commercial project.

## Data collected from Discord

The bot stores the following when you use it:

| Data | When it is stored | Why |
| --- | --- | --- |
| Your Discord user ID | The first time you run a command | Links your commands to your settings and your TypeRacer username |
| Your linked TypeRacer username | When you run `-link` | Lets you run commands without typing your username each time |
| Command usage counts | Each time you run a command | Powers `-whois` and `-commandleaderboard` |
| Timestamp of your first command | The first time you run a command | Displayed by `-whois` |
| Your preferences | When you change them | Stores your universe, embed and graph colors, date range, and command settings |

The bot does not store your Discord username, display name, avatar, email address, roles,
server memberships, or online status.

## Message content

The bot uses Discord's Message Content privileged intent because every command is a text-prefix
command, such as `-stats` or `-import keegant`. Without message content the bot cannot read which
command you ran or the arguments you gave it.

The bot only processes messages that begin with the `-` prefix. It ignores all other messages
without reading, logging, or retaining them.

Messages that begin with the prefix are recorded in a private log channel inside a Discord server
controlled by the operator. That log holds the command text you sent, your Discord user ID, and a
link back to the original message. It is used to diagnose errors and to detect abuse. This log
lives on Discord and is not copied to any system outside Discord.

Message content is never used to train machine learning or AI models, and it is never sold,
rented, or shared with third parties.

## TypeRacer data

When you run `-link` or `-import`, the bot downloads your public race history from TypeRacer's
API and stores it. This includes race times, speeds, accuracy, points, text IDs, opponent counts,
and the typing logs TypeRacer publishes for each race. All of it is data TypeRacer already
publishes for your account.

This data is keyed by TypeRacer username, not by Discord account. Anyone can request statistics
for any public TypeRacer username through the bot, whether or not that person uses Discord.

## The web server

The bot runs a small web server that renders race replay pages and handles import requests. It
records the IP address, request path, and response status of each request in the same private
Discord log channel, and keeps IP addresses in memory for up to 60 seconds to enforce rate
limits. It sets no cookies and runs no analytics or tracking scripts.

## Where data is stored

All data sits in SQLite databases on a private server rented and administered by the operator.
Access is limited to the operator.

## Third parties

The bot exchanges data with:

- **Discord**, to receive commands and send responses.
- **TypeRacer** (`play.typeracer.com`), to fetch public race and profile data.
- **TypeRacer Data** (`typeracerdata.com`), to fetch supplementary public statistics.

No data is shared with anyone else, and none of it is sold.

## Retention

Your Discord user ID, preferences, and command counts are kept until you ask for their removal.
Imported TypeRacer race data is kept indefinitely so that historical statistics stay accurate.

## Your choices

- **Stop the association.** Run `-unlink` at any time to detach your TypeRacer username from
  your Discord account.
- **Opt out entirely.** Stop running commands. The bot reads nothing else.
- **Request deletion.** Contact `@keegant` on Discord to have your stored data removed. Requests
  are handled manually.

## Children

The bot is not directed at children under 13, matching Discord's own minimum age requirement.

## Changes

Material changes to this policy are announced in the bot's changelog. The effective date above
records the most recent revision.

## Contact

Message `@keegant` on Discord, or open an issue at
https://github.com/Keegan-T/TypeRacer-Stats/issues
