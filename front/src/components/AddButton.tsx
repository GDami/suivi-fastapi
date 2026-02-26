import { useState } from "react"
import { NewApplicationModal } from "./NewApplicationModal"

type AddButtonProps = {
    text: string,
}

export function AddButton({ text }: AddButtonProps) {
    const [ open, setOpen ] = useState(false)

    const onClick = () => {
        setOpen(true)
    }

    const onClickOutside = (event: React.MouseEvent) => {
        if (event.target === event.currentTarget) {
            setOpen(false)
        }
    }

    return (
        <div>
            <button className="border p-2 cursor-pointer hover:underline" onClick={onClick}>{text}</button>
            <NewApplicationModal open={open} onClickOutside={onClickOutside} />
        </div>
    )
}