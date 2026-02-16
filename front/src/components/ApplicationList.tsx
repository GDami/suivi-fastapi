
    
export default function ApplicationList() {
    const applications = [
        { id: 1, company: "Company A", title: "Software Engineer", date: "2023-01-01", notes: "Applied via LinkedIn" },
        { id: 2, company: "Company B", title: "Product Manager", date: "2023-01-02", notes: "Applied via company website" },
    ];

    return (
        <div className="p-4">
            <h2 className="text-xl font-semibold mb-4">Applications</h2>
            <ul className="space-y-4">
                {applications.map((app) => (
                    <li key={app.id} className="border p-4 rounded shadow">
                        <div className="flex justify-between items-center">
                            <div>
                                <h3 className="font-bold">{app.title}</h3>
                                <p className="text-sm text-gray-600">{app.company}</p>
                            </div>
                            <span className="text-sm text-gray-500">{app.date}</span>
                        </div>
                        {app.notes && (
                            <p className="mt-2 text-sm text-gray-700">{app.notes}</p>
                        )}
                    </li>
                ))}
            </ul>
        </div>
    );
}