import type { ApplicationResponseModel } from "./ApplicationList";

export default function ApplicationRow(data: ApplicationResponseModel) {

    console.log(data.status)
    return (
        <li key={data.id} className="border p-4 rounded shadow">
            <div className="flex justify-between items-center">
                <div>
                    <h3 className="font-bold">{data.offer_title}</h3>
                    <p className="text-sm text-gray-600">{data.company_name}</p>
                </div>
                <span className="text-sm text-gray-500">{data.date_applied}</span>
            </div>
            {data.offer_link && (
                <a href={data.offer_link} target="_blank" rel="noopener noreferrer" className="text-sm text-blue-500 hover:underline">
                    Voir
                </a>
            )}
            {data.notes && (
                <p className="mt-2 text-sm text-gray-700">{data.notes}</p>
            )}
        </li>
    )
}