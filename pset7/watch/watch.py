import re


def main():
    # Prompt user for an HTML snippet and print the extracted short URL
    print(parse(input("HTML: ")))


def parse(s):
    """Extract and convert a YouTube iframe embed URL to a shareable youtube link."""
    # Match an HTML iframe tag containing a YouTube embed URL
    pattern = r'^<iframe [\w\d=""\s]*\s?src="(https?://)(?:w{3}\.)?(youtube)\.com/embed(/[\w\d]*)"\s?[\w\d=""\s;-]*></iframe>$'
    match = re.search(pattern, s, re.IGNORECASE)

    if match:
        # Reconstruct the base URL components from captured groups
        url = match.group(1) + match.group(2) + match.group(3)

        # Convert domain to short link format and ensure HTTPS protocol
        transformed_url = url.replace("youtube", "youtu.be").replace("http://", "https://")
        return transformed_url


if __name__ == "__main__":
    main()
