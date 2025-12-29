import { DashboardLayout } from "@/components/dashboard/DashboardLayout";

export default function Analytics() {
    return (
        <DashboardLayout>
            <div className="flex flex-col gap-6">
                <div>
                    <h2 className="text-2xl font-bold tracking-tight">Analytics</h2>
                    <p className="text-muted-foreground">Detailed error analysis and reporting.</p>
                </div>
                <div className="h-64 border-2 border-dashed rounded-lg flex items-center justify-center text-muted-foreground">
                    Coming Soon...
                </div>
            </div>
        </DashboardLayout>
    );
}
