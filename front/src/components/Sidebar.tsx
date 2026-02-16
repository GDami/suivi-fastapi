import { Link } from "react-router"

const styles = {
    h2: "text-2xl font-bold mb-4",
    li: "mb-2",
}

export default function Sidebar() {
    return (
        <aside className="w-64 h-screen bg-gray-800 text-white p-4">
            <h2 className={styles.h2}>suivi-v2</h2>
            <ul>
                <li className={styles.li}><Link to="/home" className="hover:text-gray-400">Accueil</Link></li>
                <li className={styles.li}><Link to="/applications" className="hover:text-gray-400">Candidatures</Link></li>
                {/* <li className={styles.li}><Link to="/companies" className="hover:text-gray-400">Companies</Link></li>
                <li className={styles.li}><Link to="/actions" className="hover:text-gray-400">Actions</Link></li> */}
            </ul>
        </aside>
    )
}