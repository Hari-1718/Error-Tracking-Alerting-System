import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { fetchErrors, fetchStats, triggerTestError } from "@/lib/api";
import { useToast } from "@/hooks/use-toast";
import { DashboardLayout } from "@/components/dashboard/DashboardLayout";
import { StatsCards } from "@/components/dashboard/StatsCards";
import { ErrorChart } from "@/components/dashboard/ErrorChart";
import { ErrorTable } from "@/components/dashboard/ErrorTable";
import { Button } from "@/components/ui/button";
import { RefreshCcw, Zap } from "lucide-react";

export default function Dashboard() {
    const { toast } = useToast();
    const queryClient = useQueryClient();

    // Fetch Errors
    const { data: errors = [], isLoading: errorsLoading } = useQuery({
        queryKey: ["errors"],
        queryFn: fetchErrors,
        refetchInterval: 5000,
    });

    // Calculate high-level metrics
    const totalErrors = errors.length;
    const criticalErrors = errors.filter((e: any) => e.is_critical).length;

    // Mutation for Test Error
    const mutation = useMutation({
        mutationFn: triggerTestError,
        onSuccess: () => {
            toast({
                title: "Error Triggered",
                description: "A test error was sent to the backend.",
                variant: "destructive",
            });
            queryClient.invalidateQueries({ queryKey: ["errors"] });
        },
        onError: () => {
            toast({
                title: "Failed",
                description: "Could not trigger error.",
                variant: "destructive",
            });
        }
    });

    return (
        <DashboardLayout>
            <div className="flex flex-col gap-6">

                {/* Top Control Bar */}
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                    <div>
                        <h2 className="text-2xl font-bold tracking-tight">Dashboard</h2>
                        <p className="text-muted-foreground">Monitor your application health in real-time.</p>
                    </div>
                    <div className="flex items-center gap-2">
                        <Button variant="outline" size="sm" onClick={() => queryClient.invalidateQueries()}>
                            <RefreshCcw className="mr-2 h-4 w-4" />
                            Refresh
                        </Button>
                        <Button size="sm" onClick={() => mutation.mutate()} disabled={mutation.isPending}>
                            <Zap className="mr-2 h-4 w-4" />
                            {mutation.isPending ? "Triggering..." : "Trigger Error"}
                        </Button>
                    </div>
                </div>

                {/* Metric Cards */}
                <StatsCards totalErrors={totalErrors} criticalErrors={criticalErrors} recentErrors={0} />

                {/* Charts Section */}
                <div className="grid gap-6 md:grid-cols-7">
                    <div className="md:col-span-4 lg:col-span-5">
                        <ErrorChart />
                    </div>
                    {/* We could add another small chart or list here if needed, or expand Chart */}
                </div>

                {/* Recent Errors Table */}
                <div className="space-y-4">
                    <h3 className="text-lg font-semibold">Recent Logs</h3>
                    <ErrorTable errors={errors} />
                </div>

            </div>
        </DashboardLayout>
    );
}
