import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "RayvoTech - Web Design & Development Agency",
  description: "Professional web design, UI/UX design, and SEO growth services",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
