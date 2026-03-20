'use client'

import { useEffect } from 'react'

export default function Home() {
  useEffect(() => {
    // Dynamically load the HTML content
    const loadContent = async () => {
      try {
        const response = await fetch('/temp-app/index.html')
        const html = await response.text()
        
        // Extract body content (skip DOCTYPE, html, head, body tags)
        const parser = new DOMParser()
        const doc = parser.parseFromString(html, 'text/html')
        const bodyContent = doc.body.innerHTML
        
        // Insert content into a container
        const container = document.getElementById('content-container')
        if (container) {
          container.innerHTML = bodyContent
        }
      } catch (error) {
        console.error('Failed to load content:', error)
      }
    }
    
    loadContent()
  }, [])

  return <div id="content-container" />
}
