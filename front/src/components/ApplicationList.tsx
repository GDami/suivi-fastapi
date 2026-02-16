import { useQuery } from "@tanstack/react-query";

const ApplicationStatus = {
    APPLIED: 1,
    INTERVIEWING: 2,
    REJECTED: 3,
    ACCEPTED: 4
}

type ApplicationResponseModel = {
    id: number
    cv_id: number | null
    offer_id: number
    date_applied: string
    status: keyof typeof ApplicationStatus
    notes: string | null
    offer_title: string | null
    company_name: string | null
}

type ApplicationListResponse = ApplicationResponseModel[]

const fetchApplications = async() => {
    const res = await fetch("http://localhost:8000/applications")
    return res.json()
}

export default function ApplicationList() {
    const { data, isLoading } = useQuery({
        queryKey: ["applications"],
        queryFn: fetchApplications,
    });

    console.log(data)

    if (isLoading) {
        return <div className="p-4">Loading applications...</div>;
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-semibold mb-4">Applications</h2>
            <ul className="space-y-4">
                {data.map((app: ApplicationResponseModel) => (
                    <li key={app.id} className="border p-4 rounded shadow">
                        <div className="flex justify-between items-center">
                            <div>
                                <h3 className="font-bold">{app.offer_title}</h3>
                                <p className="text-sm text-gray-600">{app.company_name}</p>
                            </div>
                            <span className="text-sm text-gray-500">{app.date_applied}</span>
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