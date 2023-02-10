
module round_robin #(parameter WID=16) (input clk, input rst_n
    ,input [WID-1:0] requests
    ,output [WID-1:0] grants
);

localparam AWID = $clog2(WID);
wire [2*WID-1:0] twice = {requests,requests};
reg [AWID-1:0] shift;

wire  [2*WID-1:0]  twice_shifted = twice >> shift;

reg [AWID-1:0] outx;
reg found;
integer ii;
always @(twice_shifted) begin
    found = 0 ;
    outx = 0;
    for (ii=0; ii<WID;ii=ii+1) begin
        if (!found && (twice_shifted[ii] == 1'b1)) begin
            found = 1;
            outx = ii;
        end
    end
end
    
wire [AWID-1:0] pos = (outx + shift) & ((1<<AWID)-1);
assign grants = {32'b0,found}<<pos;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        shift <= 0;
    end else if (found) begin
        shift <= (pos+1) & ((1<<AWID)-1);
    end
end

endmodule

