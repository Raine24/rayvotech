import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Rayvotech | Built to Elevate. Designed to Convert.',
  description: 'We design, build, and grow digital experiences that attract the right audience and turn them into paying customers.',
  openGraph: {
    type: 'website',
    url: 'https://rayvotech.com/',
    title: 'Rayvotech | Built to Elevate. Designed to Convert.',
    description: 'We design, build, and grow digital experiences that attract the right audience and turn them into paying customers.',
    images: ['https://i.imgur.com/thPnAch.png'],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Rayvotech | Built to Elevate. Designed to Convert.',
    description: 'We design, build, and grow digital experiences that attract the right audience and turn them into paying customers.',
    images: ['https://i.imgur.com/thPnAch.png'],
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&family=Space+Grotesk:wght@400;700&display=swap" rel="stylesheet" />
        <script src="https://unpkg.com/@phosphor-icons/web"></script>
        <link rel="icon" type="image/png" href="https://i.imgur.com/PYTMauh.png" />
        <script type="application/ld+json">
          {JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'ProfessionalService',
            'name': 'Rayvotech Digital',
            'url': 'https://rayvotech.com',
            'logo': 'https://i.imgur.com/thPnAch.png',
            'image': 'https://i.imgur.com/thPnAch.png',
            'description': 'We design, build, and grow digital experiences that attract the right audience and turn them into paying customers.',
            'address': {
              '@type': 'PostalAddress',
              'addressCountry': 'US'
            },
            'sameAs': [
              'https://www.facebook.com/rayvotechdigital',
              'https://www.instagram.com/rayvotech_digital/'
            ]
          })}
        </script>
      </head>
      <body className="theme-aurora">
        {children}
        <script src="/temp-app/script.js" defer />
      </body>
    </html>
  )
}
