import { Link, useLocation } from "react-router"

const styles = {
    h2: "text-2xl font-bold mb-4",
    li: "mb-2",
    currentLink: "text-white inline-block w-full",
    link: "text-gray-400 hover:text-white inline-block w-full"
}

const navLinks = [
    { name: "Accueil", path: "/home" },
    { name: "Candidatures", path: "/applications" },
    { name: "Entreprises", path: "/companies" },
    // { name: "Actions", path: "/actions" },
]

export default function Sidebar() {

    const location = useLocation();
    
    return (
        <aside className="w-64 min-h-screen bg-gray-800 text-white p-4 selection:bg-white selection:text-gray-800">
            <h2 className={styles.h2}>suivi-v2</h2>
            <ul>
                {navLinks.map((link, index) => (
                    <li key={index} className={styles.li}>
                        <Link to={link.path} className={location.pathname === link.path ? styles.currentLink : styles.link}>{link.name}</Link>
                    </li>
                ))}
            </ul>
        </aside>
    )
}