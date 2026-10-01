from fpdf import FPDF


class PDF(FPDF):
    def print_title(self):
        # Render centered header title
        self.set_font("helvetica", style='B', size=30)
        self.cell(0,
                  6,
                  "CS50 Shirtificate",
                  new_x='LMARGIN',
                  new_y="NEXT",
                  align="C",
                  )
        self.ln(4)

    def print_shirt_with_text(self, n):
        # Calculate X position to center the 150mm wide image
        image_width = 150
        space = self.w - image_width
        x = space / 2
        x_value = 0
        y_value = 100

        # Configure white text styling for overlay
        self.set_font("helvetica", style="B", size=20)
        self.set_text_color(255, 255, 255)

        # Place image and render centered overlay text
        self.image("shirtificate.png", x, 50, image_width)
        self.set_xy(x_value, y_value)
        self.cell(0,
                  10,
                  f"{n} took CS50",
                  align="C",
                  )


def main():
    # Prompt for user name
    name = input("Name: ")

    # Generate PDF document
    pdf = PDF()
    pdf.add_page()
    pdf.print_title()
    pdf.print_shirt_with_text(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
