const styles = {
    h2: "text-2xl font-bold mb-4",
    li: "mb-2",
}

export default function Sidebar() {
    return (
        <div className="w-64 h-screen bg-gray-800 text-white p-4">
            <h2 className={styles.h2}>suivi-v2</h2>
            <ul>
                <li className={styles.li}><a href="#" className="hover:text-gray-400">Home</a></li>
                <li className={styles.li}><a href="#" className="hover:text-gray-400">Applications</a></li>
                <li className={styles.li}><a href="#" className="hover:text-gray-400">Companies</a></li>
                <li className={styles.li}><a href="#" className="hover:text-gray-400">Follow-ups</a></li>
            </ul>
        </div>
    )
}