type NewApplicationModalProps = {
    open: boolean,
    onClickOutside: (event: React.MouseEvent) => void,
}

const submit = (formData: FormData) => {
    console.log("submit")
    console.log(formData.get("link"))
}

export function NewApplicationModal({ open, onClickOutside }: NewApplicationModalProps) {
    return (
        <div className={`absolute top-0 left-0 h-dvh w-dvw ${open ? 'block' : 'hidden'} bg-gray-800/50 flex justify-center items-center`} onClick={onClickOutside}>
            <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white p-4 rounded-lg">
                <h2 className="text-xl font-bold mb-4">Ajouter une candidature</h2>
                <form className="space-y-4" action={submit}>
                    <div>
                        <label htmlFor="link" className="block text-sm font-medium text-gray-700">Lien vers l'offre</label>
                        <input type="text" name="link" className="mt-1 block w-full border border-gray-300 rounded-md p-2" />
                    </div>
                    <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">Valider</button>
                </form>
            </div>
        </div>
    )
}