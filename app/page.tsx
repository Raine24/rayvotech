export default function Home() {
  return (
    <main className="min-h-screen bg-white">
      <header className="bg-black text-white p-4">
        <nav className="max-w-6xl mx-auto flex justify-between items-center">
          <h1 className="text-2xl font-bold">RayvoTech</h1>
          <ul className="flex gap-6">
            <li><a href="/" className="hover:text-gray-300">Home</a></li>
            <li><a href="/services" className="hover:text-gray-300">Services</a></li>
            <li><a href="/portfolio" className="hover:text-gray-300">Portfolio</a></li>
            <li><a href="/about" className="hover:text-gray-300">About</a></li>
            <li><a href="/contact" className="hover:text-gray-300">Contact</a></li>
          </ul>
        </nav>
      </header>

      <section className="hero bg-gradient-to-r from-blue-600 to-blue-800 text-white py-20 px-4">
        <div className="max-w-6xl mx-auto text-center">
          <h2 className="text-5xl font-bold mb-4">Welcome to RayvoTech</h2>
          <p className="text-xl mb-8">Professional Web Design, Development & SEO Growth Services</p>
          <button className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100">
            Get Started
          </button>
        </div>
      </section>

      <section className="py-20 px-4 max-w-6xl mx-auto">
        <h3 className="text-4xl font-bold mb-12 text-center">Our Services</h3>
        <div className="grid md:grid-cols-3 gap-8">
          {[
            { title: "Web Development", desc: "Custom websites built with modern technologies" },
            { title: "UI/UX Design", desc: "Beautiful and intuitive user experiences" },
            { title: "SEO & Growth", desc: "Optimize your online presence for growth" }
          ].map((service) => (
            <div key={service.title} className="border rounded-lg p-6 hover:shadow-lg transition">
              <h4 className="text-2xl font-bold mb-2">{service.title}</h4>
              <p className="text-gray-600">{service.desc}</p>
            </div>
          ))}
        </div>
      </section>

      <footer className="bg-black text-white p-8 text-center">
        <p>&copy; 2026 RayvoTech. All rights reserved.</p>
      </footer>
    </main>
  );
}
