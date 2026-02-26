import { appliedMessages } from "../dataTypes/dataTypes";
import type { ApplicationResponseModel } from "./ApplicationList";

type ApplicationRowProps = {
    applicationData: ApplicationResponseModel,
    onClick: () => void
}

export default function ApplicationRow(props: ApplicationRowProps) {
    const { applicationData: data, onClick } = props;

    const date = data.date_applied.slice(0, 10)
    return (
        <li key={data.id} className="border border-black/25 hover:bg-white shadow">
            <button className="w-full cursor-pointer text-left" onClick={onClick}>
                <div className="text-sm p-2 flex gap-2 items-center truncate">
                    <p className="max-w-80 truncate">{data.offer_title ?? "Titre de l'offre inconnu"}</p>
                    <p className="text-gray-600">|</p>
                    <p className="text-gray-600">{data.company_name ?? "Entreprise inconnue"}</p>
                    <p className="text-gray-600 grow"></p>
                    <p className="text-gray-600"><span className="font-medium">{appliedMessages[data.status] + (data.status == "status.applied" && ` le ${date}`)}</span></p>
                </div>
            </button>
        </li>
    )
}