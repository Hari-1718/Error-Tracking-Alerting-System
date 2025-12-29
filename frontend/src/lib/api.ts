export interface ErrorLog {
    _id?: string;
    api_name: string;
    status_code: number;
    error_message: string;
    timestamp: string;
    is_critical: boolean;
}

const API_BASE = "http://localhost:8000";

export async function fetchErrors(): Promise<ErrorLog[]> {
    const res = await fetch(`${API_BASE}/errors`);
    if (!res.ok) {
        throw new Error("Failed to fetch errors");
    }
    return res.json();
}

export async function fetchStats(): Promise<Record<string, number>> {
    const res = await fetch(`${API_BASE}/errors/stats`);
    if (!res.ok) {
        throw new Error("Failed to fetch stats");
    }
    return res.json();
}

export async function triggerTestError(): Promise<void> {
    await fetch(`${API_BASE}/log-error`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            api_name: "/manual-test",
            status_code: 500,
            error_message: "Manual Test Error",
            is_critical: true,
        }),
    });
}
