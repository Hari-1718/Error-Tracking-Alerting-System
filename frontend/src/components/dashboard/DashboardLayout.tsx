
import { SidebarProvider, Sidebar, SidebarContent, SidebarHeader, SidebarGroup, SidebarGroupContent, SidebarMenu, SidebarMenuItem, SidebarMenuButton, SidebarTrigger, SidebarFooter } from "@/components/ui/sidebar";
import { Home, BarChart2, Settings, ShieldAlert, User, LogOut } from "lucide-react";
import { Link, useLocation } from "wouter";

export function DashboardLayout({ children }: { children: React.ReactNode }) {
    const [location] = useLocation();

    return (
        <SidebarProvider>
            <div className="flex min-h-screen w-full bg-muted/40">
                <Sidebar className="border-r">
                    <SidebarHeader className="border-b p-4">
                        <div className="flex items-center gap-2 font-bold text-xl text-primary">
                            <ShieldAlert className="w-6 h-6" />
                            Error Sentinel
                        </div>
                    </SidebarHeader>
                    <SidebarContent>
                        <SidebarGroup>
                            <SidebarGroupContent>
                                <SidebarMenu>
                                    <SidebarMenuItem>
                                        <SidebarMenuButton asChild isActive={location === "/"}>
                                            <Link href="/">
                                                <Home />
                                                <span>Dashboard</span>
                                            </Link>
                                        </SidebarMenuButton>
                                    </SidebarMenuItem>
                                    <SidebarMenuItem>
                                        <SidebarMenuButton asChild isActive={location === "/analytics"}>
                                            <Link href="/analytics">
                                                <BarChart2 />
                                                <span>Analytics</span>
                                            </Link>
                                        </SidebarMenuButton>
                                    </SidebarMenuItem>
                                    <SidebarMenuItem>
                                        <SidebarMenuButton asChild isActive={location === "/settings"}>
                                            <Link href="/settings">
                                                <Settings />
                                                <span>Settings</span>
                                            </Link>
                                        </SidebarMenuButton>
                                    </SidebarMenuItem>
                                </SidebarMenu>
                            </SidebarGroupContent>
                        </SidebarGroup>
                    </SidebarContent>
                    <SidebarFooter className="border-t p-4">
                        <div className="flex items-center gap-2 text-sm text-muted-foreground">
                            <User className="w-4 h-4" />
                            <span>Admin</span>
                        </div>
                    </SidebarFooter>
                </Sidebar>

                <main className="flex-1 flex flex-col min-w-0 overflow-hidden">
                    <header className="flex h-14 items-center gap-4 border-b bg-background px-6 lg:h-[60px]">
                        <SidebarTrigger />
                        <div className="w-full flex-1">
                            {/* Breadcrumbs or search could go here */}
                            <h1 className="font-semibold text-lg">Overview</h1>
                        </div>
                    </header>
                    <div className="flex-1 overflow-auto p-4 md:p-6 lg:p-8">
                        {children}
                    </div>
                </main>
            </div>
        </SidebarProvider>
    );
}
