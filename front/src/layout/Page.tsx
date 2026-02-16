import type { PropsWithChildren } from "react";

export default function Page({ children }: PropsWithChildren) {
    return (
        <main className="w-full bg-gray-100">
            <div className="p-4 w-full max-w-5xl ">
                { children }
            </div>
        </main>
    )
}