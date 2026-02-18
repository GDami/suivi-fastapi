import { useQuery } from "@tanstack/react-query";
import ApplicationRow from "./ApplicationRow";

type ApplicationStatus = {
    APPLIED: "Applied",
    INTERVIEWING: "Interviewing",
    REJECTED: "Rejected",
    ACCEPTED: "Accepted"
}

export type ApplicationResponseModel = {
    id: number
    cv_id: number | null
    offer_id: number
    date_applied: string
    status: ApplicationStatus
    notes: string | null
    offer_title: string | null
    offer_link: string | null
    company_name: string | null
}

type ApplicationListResponse = ApplicationResponseModel[]

const fetchApplications = async(): Promise<ApplicationListResponse> => {
    const res = await fetch("http://localhost:8000/applications")
    return res.json()
}

export default function ApplicationList() {
    const { data, isLoading, isError } = useQuery({
        queryKey: ["applications"],
        queryFn: fetchApplications,
        initialData: [],
    });

    if (isLoading) {
        return <div className="p-4">Loading applications...</div>;
    }

    if (isError) {
        return <div className="p-4 text-red-500">Error fetching applications.</div>;
    }

    return (
        <div className="p-4">
            <h2 className="text-xl font-semibold mb-4">Candidatures ({data.length})</h2>
            <ul className="space-y-4">
                {data.map((app: ApplicationResponseModel) => (
                    <ApplicationRow key={app.id} {...app} />
                ))}
            </ul>
        </div>
    );
}