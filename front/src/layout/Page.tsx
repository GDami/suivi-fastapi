import type { PropsWithChildren } from "react";

export default function Page({ children }: PropsWithChildren) {
    return (
        <main className="p-4 w-full max-w-5xl bg-gray-100">
            { children }
        </main>
    )
}