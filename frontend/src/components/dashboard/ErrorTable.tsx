
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";
import { Copy, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { type ErrorLog } from "@/lib/api";
import { format } from "date-fns";

interface ErrorTableProps {
    errors: ErrorLog[];
}

export function ErrorTable({ errors }: ErrorTableProps) {
    return (
        <div className="rounded-md border bg-card">
            <Table>
                <TableHeader>
                    <TableRow>
                        <TableHead className="w-[100px]">Status</TableHead>
                        <TableHead>Error Message</TableHead>
                        <TableHead>API Service</TableHead>
                        <TableHead className="hidden md:table-cell">Time</TableHead>
                        <TableHead className="text-right">Actions</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    {errors.length === 0 ? (
                        <TableRow>
                            <TableCell colSpan={5} className="h-24 text-center">
                                No errors found (yet!)
                            </TableCell>
                        </TableRow>
                    ) : (
                        errors.map((error, i) => (
                            <TableRow key={error._id || i}>
                                <TableCell>
                                    <Badge
                                        variant={error.status_code >= 500 ? "destructive" : "secondary"}
                                        className="font-mono text-xs"
                                    >
                                        {error.status_code}
                                    </Badge>
                                </TableCell>
                                <TableCell className="font-medium max-w-[300px] truncate" title={error.error_message}>
                                    <div className="flex items-center gap-2">
                                        {error.is_critical && <AlertCircle className="w-4 h-4 text-red-500" />}
                                        {error.error_message}
                                    </div>
                                </TableCell>
                                <TableCell className="text-muted-foreground">{error.api_name}</TableCell>
                                <TableCell className="hidden md:table-cell text-muted-foreground">
                                    {error.timestamp ? format(new Date(error.timestamp), "MMM dd, HH:mm") : "-"}
                                </TableCell>
                                <TableCell className="text-right">
                                    <Button variant="ghost" size="icon" onClick={() => navigator.clipboard.writeText(JSON.stringify(error, null, 2))}>
                                        <Copy className="h-4 w-4" />
                                    </Button>
                                </TableCell>
                            </TableRow>
                        ))
                    )}
                </TableBody>
            </Table>
        </div>
    );
}
